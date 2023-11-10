from django.contrib import admin
from .models import TraineeInfo, Exercises, WorkoutLog

# Register your models here.


@admin.register(TraineeInfo)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_date', 'age', 'weight', 'height')
    list_filter = ('name',)
