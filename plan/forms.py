from django import forms
from .models import TraineeInfo, WorkoutLog


class TraineeInfoForm(forms.ModelForm):
    class Meta:
        model = TraineeInfo
        fields = ('name', 'age', 'weight', 'height', 'sex', 'goal')
        labels = {
            'sex': 'Sex (If you prefere not to disclose, please select neutral)',
            'goal': 'Please select a goal'
        }


class LogExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ('sets_actual', 'reps_actual')
        labels = {
            'sets_actual': 'How many sets?',
            'reps_actual': 'How many reps per set?'
        }
