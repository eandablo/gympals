from django.shortcuts import render, get_object_or_404, reverse
from django.views import View, generic
from .forms import TraineeInfoForm, LogExerciseForm
from .models import TraineeInfo, WorkoutLog, Diet
from django.http import HttpResponseRedirect
from .decisions import WorkoutGen, DietGen


class HomeView(View):

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
             "info_form": TraineeInfoForm()}
        )

    def post(self, request, *args, **kwargs):
        info_form = TraineeInfoForm(data=request.POST)
        new_trainee = request.user
        info_exists = False
        if info_form.is_valid():
            info = info_form.save(commit=False)
            info.trainee = new_trainee
            info.save()
            info_exists = True
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
        if not WorkoutLog.objects.filter(trainee__name=name, completed=False):
            self.select_ids(name)
        calories = self.calories_calc(name)
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
             "update_form": LogExerciseForm(),
             "name": name}
        )


class LogWorkout(View):
    def post(self, request, log_id, *args, **kwargs):
        log = get_object_or_404(WorkoutLog, id=log_id)
        form = LogExerciseForm(data=request.POST, instance=log)
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
             "log_type": log_type}
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


class UpdateInfo(View):
    def get(self, request, name, *args, **kwargs):
        trainee = get_object_or_404(TraineeInfo, name=name)
        info_form = TraineeInfoForm(instance=trainee)
        return render(
            request,
            'update_info.html',
            {"info_form": info_form}
        )

    def post(self, request, name, *args, **kwargs):
        trainee = get_object_or_404(TraineeInfo, name=name)
        info_form = TraineeInfoForm(data=request.POST, instance=trainee)
        if info_form.is_valid:
            info_form.save()

        return HttpResponseRedirect(reverse('home'))
