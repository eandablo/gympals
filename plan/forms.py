from django import forms
from .models import TraineeInfo


class TraineeInfoForm(forms.ModelForm):
    class Meta:
        model = TraineeInfo
        fields = ('name', 'age', 'weight', 'height')
