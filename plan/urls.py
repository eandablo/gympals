from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('plan/<name>', views.WorkoutView.as_view(), name='workout_plan'),
    path('update/<log_id>', views.LogWorkout.as_view(), name='update_workout'),
    path('workoutlogs/<name>', views.WLogViews.as_view(), name='wlogs_view'),
    path('dietlogs/<name>', views.WLogViews.as_view(), name='dlogs_view'),
    path('info/<name>', views.UpdateInfo.as_view(), name='info_update'),
]
