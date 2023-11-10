from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('plan/<name>', views.WorkoutView.as_view(), name='workout_plan')
]
