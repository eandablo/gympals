from django import forms
from .models import TraineeInfo


class TraineeInfoForm(forms.ModelForm):
    class Meta:
        model = TraineeInfo
        fields = ('name', 'updated_date', 'age', 'weight', 'height')


