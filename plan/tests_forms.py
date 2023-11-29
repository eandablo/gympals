from django.test import TestCase
from . import forms


class TestTraineeInfoForm(TestCase):
    def test_name_field_is_required(self):
        form = forms.TraineeInfoForm(
            {'name': '',
             'age': 1,
             'weight': 3,
             'height': 4,
             'sex': 'F',
             'goal': 'WL'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_age_field_is_required(self):
        form = forms.TraineeInfoForm(
            {'name': 'user',
             'age': '',
             'weight': 3,
             'height': 4,
             'sex': 'F',
             'goal': 'WL'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors.keys())
        self.assertEqual(form.errors['age'][0], 'This field is required.')

    def test_weight_field_is_required(self):
        form = forms.TraineeInfoForm(
            {'name': 'user',
             'age': 1,
             'weight': '',
             'height': 4,
             'sex': 'F',
             'goal': 'WL'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('weight', form.errors.keys())
        self.assertEqual(form.errors['weight'][0], 'This field is required.')

    def test_height_field_is_required(self):
        form = forms.TraineeInfoForm(
            {'name': 'user',
             'age': 1,
             'weight': 20,
             'height': '',
             'sex': 'F',
             'goal': 'WL'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('height', form.errors.keys())
        self.assertEqual(form.errors['height'][0], 'This field is required.')
