from django.contrib import admin
from .models import TraineeInfo, Exercises, WorkoutLog

# Register your models here.


@admin.register(TraineeInfo)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_date', 'age', 'weight', 'height')
    list_filter = ('name',)


@admin.register(Exercises)   
class ExerciseInfo(admin.ModelAdmin):
    list_display = ('name', 'guide_image', 'muscle_group', 'youtube_link')
    list_filter = ('muscle_group',)


@admin.register(WorkoutLog)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'created_date',
                    'trainee', 'logged_date', 'sets_ideal',
                    'sets_actual', 'reps_ideal', 'reps_actual',
                    'completed', 'excercise')
    list_filter = ('trainee',)
