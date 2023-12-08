from django import forms
from .models import TraineeInfo, WorkoutLog, Exercises


class TraineeInfoForm(forms.ModelForm):
    class Meta:
        model = TraineeInfo
        fields = ('name', 'age', 'weight', 'height', 'sex', 'goal')
        labels = {
            'weight': 'Weight (Kg)',
            'height': 'Height (cm)',
            'sex': 'Sex (If you prefere not to disclose,' +
            'please select neutral)',
            'goal': 'Please select a goal'
        }


class UpdateInfoForm(forms.ModelForm):
    class Meta:
        model = TraineeInfo
        fields = ('age', 'weight', 'height', 'goal')
        labels = {
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


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercises
        fields = ('name', 'guide_image', 'muscle_group', 'youtube_link',
                  'level', 'calories_burnt', 'gender')
        labels = {
            'guide_image': 'Image',
            'muscle_group': 'Muscle Group',
            'youtube_link': 'Youtube URL',
            'calories_burnt': 'Expected Calories Burnt',
            'gender': 'Best Suited For (Sex):'
        }
