from django.shortcuts import render, get_object_or_404, reverse
from django.views import View, generic
from . import forms
from .models import TraineeInfo, WorkoutLog, Diet, Exercises
from django.http import HttpResponseRedirect
from .decisions import WorkoutGen, DietGen, SiteAnalysis
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import date


class HomeView(View, SiteAnalysis):
    '''
    Get function displays index page
    If user has information displays dashborad
    otherwise display the form to store user info
    '''
    def get(self, request, *args, **kwargs):
        # Staff users are redirected to a dashboard with link
        # to see the exercise catalog
        if request.user.is_staff:
            trainees_data = self.total_trainees()
            exercise_data = self.exercises_describe()
            performance = self.calc_performance()
            return render(
                request,
                'index.html',
                {"performance": performance,
                 "exercise_data": exercise_data,
                 "trainees_data": trainees_data}
            )

        else:
            info_exists = False
            # Normal users returning are redirected to their dashboard
            if hasattr(request.user, 'traineeinfo'):
                info_exists = True
                trainee = get_object_or_404(
                    TraineeInfo, trainee=request.user)
                return render(
                    request,
                    'index.html',
                    {"info_exists": info_exists,
                     "trainee": trainee}
                )
            # Normal user just signed-up is prompted to info form
            else:
                return render(
                    request,
                    'index.html',
                    {"info_exists": info_exists,
                     "info_form": forms.TraineeInfoForm()}
                )

    '''
    Manages the TraineeInfo form post
    '''
    def post(self, request, *args, **kwargs):
        info_form = forms.TraineeInfoForm(data=request.POST)
        new_trainee = request.user
        info_exists = False
        names = TraineeInfo.objects.values_list('name')

        if info_form.is_valid():
            info = info_form.save(commit=False)
            info.trainee = new_trainee
            info.save()
            info_exists = True
            trainee = get_object_or_404(TraineeInfo, trainee=request.user)
            messages.success(request, 'Information Succesfully Added')
        else:
            messages.error(request, 'Name already exists')
            return render(
                request,
                'index.html',
                {"info_exists": info_exists,
                 "info_form": forms.TraineeInfoForm()}
            )

        return render(
            request,
            'index.html',
            {"trainee": trainee,
             "info_exists": info_exists}
        )


class WorkoutView(View, WorkoutGen, DietGen):
    '''
    Displays workout for user in 'workout_plan.html'
    Finds entries of WorkoutLog model with completed = False
    if none, creates a workout plan for user calling
    select_ids function from Mixin WorkoutGen
    additionally recalculates diet using DietGen
    '''
    def get(self, request, name, *args, **kwargs):
        logs = WorkoutLog.objects.filter(trainee__name=name, completed=False)
        if not logs:
            self.select_ids(name)
            self.calories_calc(name)
            logs = WorkoutLog.objects.filter(
                trainee__name=name, completed=False)
        days = logs.order_by('day').values_list('day').distinct('day')
        ids = []
        # Ids contain information for workout page accordion item
        for day in days:
            labels = ['#accordion-'+str(day[0]),
                      'accordion-'+str(day[0]), day[0]]
            ids.append(labels)

        return render(
            request,
            'workout_plan.html',
            {"logs": logs,
             "ids": ids,
             "name": name}
        )


class LogWorkout(View):
    '''
    Manages the user post of sets and reps in forms.LogExerciseForm
    redirects to workout_plan.html
    '''
    def post(self, request, log_id, *args, **kwargs):
        log = get_object_or_404(WorkoutLog, id=log_id)
        sets = request.POST.get('sets' + log.excercise.name)
        reps = request.POST.get('reps' + log.excercise.name)
        print(reps)
        log.sets_actual = int(sets)
        log.reps_actual = int(reps)
        log.completed = True
        log.save()
        # If the last exercise is logged, it redirects to home
        # otherwise redirects to workout plan
        if WorkoutLog.objects.filter(trainee=log.trainee, completed=False):
            return HttpResponseRedirect(reverse('workout_plan',
                                        args=[log.trainee.name]))
        else:
            return HttpResponseRedirect(reverse('home'))


class WLogViews(View):
    '''
    Displays completed entries of WorkoutLog in logs_view.html
    '''
    def get(self, request, name, page, *args, **kwargs):
        log_type = 'workout'
        logs = WorkoutLog.objects.filter(trainee__name=name, completed=True)
        paginator = Paginator(logs, 5)
        page_obj = paginator.get_page(page)
        return render(
            request,
            'logs_view.html',
            {"logs": page_obj,
             "log_type": log_type,
             "name": name}
        )

    '''
    Displays completed entries of WorkoutLog in logs_view.html
    narrowing entries to selected dates
    '''
    def post(self, request, name, page, *args, **kwargs):
        log_type = 'workout'
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if start_date < end_date:
            logs = WorkoutLog.objects.filter(trainee__name=name,
                                             completed=True,
                                             logged_date__range=[start_date,
                                                                 end_date])
        else:
            messages.info(request, 'Start date should predate the End date')
            logs = WorkoutLog.objects.filter(
                trainee__name=name, completed=True)

        paginator = Paginator(logs, 5)
        page_obj = paginator.get_page(page)
        return render(
            request,
            'logs_view.html',
            {"logs": page_obj,
             "log_type": log_type,
             "name": name}
        )


class DLogViews(View):
    '''
    Displays entries of DietLog in logs_view.html
    '''
    def get(self, request, name, page, *args, **kwargs):
        log_type = 'diet'
        logs = Diet.objects.filter(trainee__name=name)
        trainee = TraineeInfo.objects.get(name=name)
        paginator = Paginator(logs, 5)
        page_obj = paginator.get_page(page)
        # Variable to display diet log input
        if trainee.calories:
            up_to_date = False
        else:
            up_to_date = True

        today_date = date.today()
        log_today = Diet.objects.filter(trainee__name=name,
                                        created_date=today_date).exists()
        if log_today:
            up_to_date = True

        return render(
            request,
            'logs_view.html',
            {"logs": page_obj,
             "log_type": log_type,
             "name": name,
             "up_to_date": up_to_date}
        )

    '''
    Displays entries of DietLog in logs_view.html
    narrowing entries to selected dates
    '''
    def post(self, request, name, page, *args, **kwargs):
        log_type = 'diet'
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if start_date < end_date:
            logs = Diet.objects.filter(trainee__name=name,
                                       logged_date__range=[start_date,
                                                           end_date])
        else:
            logs = Diet.objects.filter(
                trainee__name=name)
            messages.info(request, 'Start date should predate the End date')

        paginator = Paginator(logs, 5)
        page_obj = paginator.get_page(page)
        # Variable to display diet log input
        if trainee.calories:
            up_to_date = False
        else:
            up_to_date = True
        today_date = date.today()
        log_today = Diet.objects.filter(trainee__name=name,
                                        created_date=today_date).exists()
        if log_today:
            up_to_date = True

        return render(
            request,
            'logs_view.html',
            {"logs": page_obj,
             "log_type": log_type,
             "name": name,
             "up_to_date": up_to_date}
        )


class UpdateInfo(View, DietGen):
    '''
    Displays form UpdateInfoForm in update_info.html
    '''
    def get(self, request, name, *args, **kwargs):
        trainee = get_object_or_404(TraineeInfo, name=name)
        info_form = forms.UpdateInfoForm(instance=trainee)
        return render(
            request,
            'update_info.html',
            {"info_form": info_form}
        )

    '''
    Manages UpdateInfoForm user posting from update_info.html
    redirects to index.html if form is valid after saving the entry
    '''
    def post(self, request, name, *args, **kwargs):
        trainee = get_object_or_404(TraineeInfo, name=name)
        info_form = forms.UpdateInfoForm(data=request.POST, instance=trainee)
        if info_form.is_valid:
            info_form.save()
            self.calories_calc(name)
            messages.success(request, 'Your information has been updated')
        else:
            messages.error(request, 'Please provide valid information')
            return render(
                request,
                'update_info.html',
                {"info_form": forms.UpdateInfoForm(instance=trainee)}
            )

        return HttpResponseRedirect(reverse('home'))


class UpdateDietLogs(View):
    def post(self, request, name, *args, **kwargs):
        trainee = get_object_or_404(TraineeInfo, name=name)
        calories_ideal = trainee.calories
        calories = request.POST.get('diet_input')
        today_date = date.today()
        log_today = Diet.objects.filter(trainee__name=name,
                                        created_date=today_date).exists()
        if not log_today:
            Diet.objects.create(trainee=trainee,
                                calories=calories,
                                calories_ideal=calories_ideal)
            messages.success(request, 'Your diet records are updated')
        else:
            messages.error(request, 'A log for this day already exist')

        return HttpResponseRedirect(reverse('dlogs_view', args=[name, 1]))

# Views for the Admin


class CatalogView(View):
    '''
    Shows exercises in catalog.html divided in accordions
    by muscle groups
    '''
    def get(self, request, *args, **kwargs):
        groups = Exercises.objects.order_by(
            'muscle_group').values_list(
                'muscle_group').distinct('muscle_group')
        logs = Exercises.objects.all()
        ids = []
        for group in groups:
            labels = ['#accordion-'+str(group[0]),
                      'accordion-'+str(group[0]), group[0]]
            ids.append(labels)

        return render(
            request,
            'catalog.html',
            {"ids": ids,
             "logs": logs,
             "exercise_form": forms.CreateExerciseForm()}
        )
    '''
    Manages the form to add exercises in calalog.html
    '''
    def post(self, request, *args, **kwargs):
        exercise_form = forms.CreateExerciseForm(request.POST, request.FILES)
        logs = Exercises.objects.all()
        names_top = logs.values_list('name')
        names = [name[0] for name in names_top]
        if exercise_form.is_valid():
            exercise_form.save()
            messages.success(request, 'New Exercise Added')
        else:
            messages.error(request, 'Name already exists')
        groups = Exercises.objects.order_by(
            'muscle_group').values_list(
                'muscle_group').distinct('muscle_group')
        logs = Exercises.objects.all()
        ids = []
        # Creates labels for accordions in catalog.html
        for group in groups:
            labels = ['#accordion-'+str(group[0]),
                      'accordion-'+str(group[0]), group[0]]
            ids.append(labels)

        return render(
            request,
            'catalog.html',
            {"ids": ids,
             "logs": logs,
             "exercise_form": forms.CreateExerciseForm()}
        )


class EditExercise(View):
    '''
    Shows exercise with exercise_id and the number of user currently
    displaying this exercise in their workout plan
    Displays a form to edit the exercise
    '''
    def get(self, request, exercise_id, *args, **kwargs):
        exercise = get_object_or_404(Exercises, id=exercise_id)
        # calculates number of workoutlogs for the exercise not completed
        n_users = WorkoutLog.objects.filter(completed=False,
                                            excercise__id=exercise_id).count()
        exercise_form = forms.CreateExerciseForm(instance=exercise)
        return render(
            request,
            'exercise_edit.html',
            {"n_users": n_users,
             "exercise": exercise,
             "exercise_form": exercise_form}
        )

    '''
    Manages edit exercise form
    send success message if form is successfully logged
    '''
    def post(self, request, exercise_id, *args, **kwargs):
        exercise = get_object_or_404(Exercises, id=exercise_id)
        exercise_form = forms.CreateExerciseForm(request.POST,
                                                 request.FILES,
                                                 instance=exercise)
        if exercise_form.is_valid():
            exercise_form.save()
            messages.success(request, 'Exercise successfully edited')
        else:
            messages.error(request, 'Data provided is not valid')
            n_users = WorkoutLog.objects.filter(
                completed=False,
                excercise__id=exercise_id).count()
            exercise_form = forms.CreateExerciseForm(instance=exercise)
            return render(
                request,
                'exercise_edit.html',
                {"n_users": n_users,
                 "exercise": exercise,
                 "exercise_form": exercise_form}
            )
        return HttpResponseRedirect(reverse('catalog'))


class DeleteExercise(View):
    '''
    Deletes the exercises with the selected id
    and redirects to cataglo.html if the correct entry in provided
    in the text input with name input_name otherwise redirects
    to edit_exercise.html and send error message
    '''
    def post(self, request, id, *args, **kwargs):
        exercise = get_object_or_404(Exercises, id=id)
        input_name = request.POST.get('delete_code')
        if input_name == exercise.name:
            exercise.delete()
            messages.success(request, 'Exercise Deleted')
        else:
            messages.error(request, 'Text Do Not Concides')
            return HttpResponseRedirect(reverse('edit_exercise',
                                                args=[exercise.id]))

        return HttpResponseRedirect(reverse('catalog'))
