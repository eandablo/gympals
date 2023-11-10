from django.shortcuts import render
from django.views import View
from .forms import TraineeInfoForm


class HomeView(View):

    def get(self, request, *args, **kwargs):
        info_exists = False
        if hasattr(request.user, 'traineeinfo'):
            info_exists = True

        return render(
            request,
            'index.html',
            {"info_exists": info_exists,
             "info_form": TraineeInfoForm()}
        )

    def post(self, request, *args, **kwargs):
        info_form = TraineeInfoForm(data=request.POST)
        new_trainee = request.user
        info_exists = False
        if info_form.is_valid():
            info_form.instance.trainee = new_trainee
            info_form.save()
            info_exists = True
        return render(
            request,
            'index.html',
            {"info_exists": info_exists}
        )
