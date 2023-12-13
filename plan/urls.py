from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('plan/<name>', views.WorkoutView.as_view(), name='workout_plan'),
    path('update/<log_id>', views.LogWorkout.as_view(), name='update_workout'),
    path('workoutlogs/<name>/<int:page>',
         views.WLogViews.as_view(), name='wlogs_view'),
    path('workoutlogs_p/<name>/<int:page>',
         views.PaginationWViews.as_view(), name='wlogs_p_view'),
    path('dietlogs/<name>/<int:page>',
         views.DLogViews.as_view(), name='dlogs_view'),
    path('dietlogs_p/<name>/<int:page>',
         views.PaginationDViews.as_view(), name='dlogs_p_view'),
    path('dietupdate/<name>',
         views.UpdateDietLogs.as_view(), name='diet_update'),
    path('info/<name>', views.UpdateInfo.as_view(), name='info_update'),
    path('catalog', views.CatalogView.as_view(), name='catalog'),
    path('edit_exercise/<exercise_id>',
         views.EditExercise.as_view(), name='edit_exercise'),
    path('delete/<id>', views.DeleteExercise.as_view(), name='delete_exercise')
]
