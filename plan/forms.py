from django import forms
from .models import TraineeInfo, WorkoutLog


class TraineeInfoForm(forms.ModelForm):
    class Meta:
        model = TraineeInfo
        fields = ('name', 'age', 'weight', 'height')


class LogExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ('sets_actual', 'reps_actual', 'completed')
