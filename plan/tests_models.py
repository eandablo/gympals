from django.test import TestCase
from . import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestTraineeInfo(TestCase):
    def test_sex_field_defaults_N(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        item = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        self.assertEqual(item.sex, 'N')

    def test_goal_field_defaults_WL(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        item = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        self.assertEqual(item.goal, 'WL')

    def test_str_method_returns_name(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        item = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        self.assertEqual(str(item), 'Person')


class TestExercises(TestCase):
    def test_guide_image_defaults_none(self):
        item = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        self.assertEqual(item.guide_image, 'None')

    def test_image_link_defaults_none(self):
        item = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        self.assertEqual(item.youtube_link, 'None')

    def test_level_defaults_1(self):
        item = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        self.assertEqual(item.level, 1)

    def test_calories_burnt_defaults_0(self):
        item = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        self.assertEqual(item.calories_burnt, 0)

    def test_gender_defaults_N(self):
        item = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        self.assertEqual(item.gender, 'B')

    def test_str_method_returns_name(self):
        item = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        self.assertEqual(str(item), 'exercise: Test')
