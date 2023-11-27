from django.shortcuts import render, get_object_or_404, reverse
from django.views import View, generic
from . import forms
from .models import TraineeInfo, WorkoutLog, Diet, Exercises
from django.http import HttpResponseRedirect
from .decisions import WorkoutGen, DietGen


class HomeView(View, WorkoutGen, DietGen):

    def get(self, request, *args, **kwargs):
        info_exists = False
        trainee = request.user
        if hasattr(request.user, 'traineeinfo'):
            info_exists = True
            trainee = get_object_or_404(TraineeInfo, trainee=request.user)
        return render(
            request,
            'index.html',
            {"info_exists": info_exists,
             "trainee": trainee,
             "info_form": forms.TraineeInfoForm()}
        )

    def post(self, request, *args, **kwargs):
        info_form = forms.TraineeInfoForm(data=request.POST)
        new_trainee = request.user
        info_exists = False
        if info_form.is_valid():
            info = info_form.save(commit=False)
            info.trainee = new_trainee
            info.save()
            info_exists = True
            trainee = get_object_or_404(TraineeInfo, trainee=request.user)
            name = trainee.name
            self.select_ids(name)
            self.calories_calc(name)
            trainee = get_object_or_404(TraineeInfo, trainee=request.user)

        return render(
            request,
            'index.html',
            {"trainee": trainee,
             "info_exists": info_exists}
        )


class WorkoutView(View, WorkoutGen, DietGen):
    def get(self, request, name, *args, **kwargs):
        logs = WorkoutLog.objects.filter(trainee__name=name, completed=False)
        if not logs:
            self.select_ids(name)
            self.calories_calc(name)
        days = logs.order_by('day').values_list('day').distinct('day')
        ids = []
        for day in days:
            labels = ['#accordion-'+str(day[0]),
                      'accordion-'+str(day[0]), day[0]]
            ids.append(labels)

        return render(
            request,
            'workout_plan.html',
            {"logs": logs,
             "ids": ids,
             "update_form": forms.LogExerciseForm(),
             "name": name}
        )


class LogWorkout(View):
    def post(self, request, log_id, *args, **kwargs):
        log = get_object_or_404(WorkoutLog, id=log_id)
        form = forms.LogExerciseForm(data=request.POST, instance=log)
        if form.is_valid():
            form.instance.completed = True
            form.save()
        return HttpResponseRedirect(reverse('workout_plan',
                                    args=[log.trainee.name]))


class WLogViews(View):
    def get(self, request, name, *args, **kwargs):
        log_type = 'workout'
        logs = WorkoutLog.objects.filter(trainee__name=name, completed=True)
        return render(
            request,
            'logs_view.html',
            {"logs": logs,
             "log_type": log_type,
             "name": name}
        )

    def post(self, request, name, *args, **kwargs):
        log_type = 'workout'
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        logs = WorkoutLog.objects.filter(trainee__name=name, completed=True,
                                         logged_date__range=[start_date,
                                                             end_date])
        return render(
            request,
            'logs_view.html',
            {"logs": logs,
             "log_type": log_type,
             "name": name,
             "date": start_date}
        )


class DLogViews(View):
    def get(self, request, name, *args, **kwargs):
        log_type = 'diet'
        logs = Diet.objects.filter(trainee__name=name)
        return render(
            request,
            'logs_view.html',
            {"logs": logs,
             "log_type": log_type,
             "name": name}
        )

    def post(self, request, name, *args, **kwargs):
        log_type = 'diet'
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        logs = Diet.objects.filter(trainee__name=name, completed=True,
                                   logged_date__range=[start_date,
                                                       end_date])
        return render(
            request,
            'logs_view.html',
            {"logs": logs,
             "log_type": log_type,
             "name": name,
             "date": start_date}
        )


class UpdateInfo(View, DietGen):
    def get(self, request, name, *args, **kwargs):
        trainee = get_object_or_404(TraineeInfo, name=name)
        info_form = forms.UpdateInfoForm(instance=trainee)
        return render(
            request,
            'update_info.html',
            {"info_form": info_form}
        )

    def post(self, request, name, *args, **kwargs):
        trainee = get_object_or_404(TraineeInfo, name=name)
        info_form = forms.UpdateInfoForm(data=request.POST, instance=trainee)
        if info_form.is_valid:
            info_form.save()
            self.calories_calc(name)

        return HttpResponseRedirect(reverse('home'))


class CatalogView(View):
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

    def post(self, request, *args, **kwargs):
        exercise_form = forms.CreateExerciseForm(request.POST, request.FILES)
        if exercise_form.is_valid:
            exercise_form.save()
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


class EditExercise(View):
    def get(self, request, exercise_id, *args, **kwargs):
        exercise = get_object_or_404(Exercises, id=exercise_id)
        exercise_form = forms.CreateExerciseForm(instance=exercise)
        return render(
            request,
            'exercise_edit.html',
            {"exercise": exercise,
             "exercise_form": exercise_form}
        )

    def post(self, request, exercise_id, *args, **kwargs):
        exercise = get_object_or_404(Exercises, id=exercise_id)
        exercise_form = forms.CreateExerciseForm(request.POST,
                                                 request.FILES,
                                                 instance=exercise)
        if exercise_form.is_valid():
            exercise_form.save()

        return HttpResponseRedirect(reverse('catalog'))


class DeleteExercise(View):
    def post(self, request, id, *args, **kwargs):
        exercise = get_object_or_404(Exercises, id=id)
        input_name = request.POST.get('delete_code')
        if input_name == exercise.name:
            exercise.delete()
        else:
            return HttpResponseRedirect(reverse('edit_exercise',
                                                args=[exercise.id]))            

        return HttpResponseRedirect(reverse('catalog'))
