from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from .forms import TraineeInfoForm
from .models import TraineeInfo, WorkoutLog


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


class WorkoutView(View):
    def get(self, request, name, *args, **kwargs):
        logs = WorkoutLog.objects.filter(trainee__name=name, completed=False)
        days = logs.order_by('day').values_list('day').distinct('day')
        ids = []
        for day in days:
            labels = ['#accordion-'+str(day[0]), 'accordion-'+str(day[0])]
            ids.append(labels)

        return render(
            request,
            'workout_plan.html',
            {"logs": logs,
             "ids": ids}
        )


class LogViews(generic.ListView):
    def get(self, request, name, *args, **kwargs):
        logs = WorkoutLog.objects.filter(trainee__name=name, completed=True)
        return render(
            request,
            'logs_view.html',
            {"logs": logs}
        )
