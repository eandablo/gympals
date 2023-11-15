from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('plan/<name>', views.WorkoutView.as_view(), name='workout_plan'),
    path('update/<log_id>', views.LogWorkout.as_view(), name='update_workout'),
    path('logs/<name>', views.LogViews.as_view(), name='logs_view'),
]
