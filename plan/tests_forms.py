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


class TestUpdateInfoForm(TestCase):
    def test_age_field_is_required(self):
        form = forms.UpdateInfoForm(
            {'age': '',
             'weight': 3,
             'height': 4,
             'sex': 'F',
             'goal': 'WL'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors.keys())
        self.assertEqual(form.errors['age'][0], 'This field is required.')

    def test_weight_field_is_required(self):
        form = forms.UpdateInfoForm(
            {'age': 1,
             'weight': '',
             'height': 4,
             'sex': 'F',
             'goal': 'WL'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('weight', form.errors.keys())
        self.assertEqual(form.errors['weight'][0], 'This field is required.')

    def test_height_field_is_required(self):
        form = forms.UpdateInfoForm(
            {'age': 1,
             'weight': 20,
             'height': '',
             'sex': 'F',
             'goal': 'WL'}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('height', form.errors.keys())
        self.assertEqual(form.errors['height'][0], 'This field is required.')


class TestCreateExerciseForm(TestCase):
    def test_name_is_required(self):
        form = forms.CreateExerciseForm(
            {'name': '',
             'youtube_link': 'some_link',
             'muscle_group': 'BACK',
             'level': 1,
             'calories_burnt': 5,
             'gender': 'M'}
        )
        self.assertFalse(form.is_valid())

    def test_youtube_link_is_required(self):
        form = forms.CreateExerciseForm(
            {'name': 'tester',
             'youtube_link': '',
             'muscle_group': 'BACK',
             'level': 1,
             'calories_burnt': 5,
             'gender': 'M'}
        )
        self.assertFalse(form.is_valid())

    def test_calories_burnt_is_required(self):
        form = forms.CreateExerciseForm(
            {'name': 'tester',
             'youtube_link': 'some_link',
             'muscle_group': 'BACK',
             'level': 1,
             'calories_burnt': '',
             'gender': 'M'}
        )
        self.assertFalse(form.is_valid())
