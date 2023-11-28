from django.test import TestCase
from . import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from datetime import date


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

    def test_date_updates(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        item = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        date_today = date.today()
        self.assertEqual(item.updated_date, date_today)

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


class TestWorkoutLog(TestCase):
    def test_day_defaults_1(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        self.assertEqual(item.day, 1)

    def test_created_date_is_today(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        date_today = date.today()
        self.assertEqual(item.created_date, date_today)

    def test_logged_date_is_today(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        date_today = date.today()
        self.assertEqual(item.logged_date, date_today)

    def test_sets_ideal_defaults_0(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        self.assertEqual(item.sets_ideal, 0)

    def test_sets_actual_defaults_0(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        self.assertEqual(item.sets_actual, 0)

    def test_reps_ideal_defaults_0(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        self.assertEqual(item.reps_ideal, 0)

    def test_reps_actual_defaults_0(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        self.assertEqual(item.reps_actual, 0)

    def test_completed_defaults_False(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        self.assertEqual(item.completed, False)

    def test_string_returns_trainee_name(self):
        exercise = models.Exercises.objects.create(
            name='Test',
            muscle_group='BACK',
        )
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.WorkoutLog.objects.create(
            identifier='week1',
            trainee=trainee,
            excercise=exercise
        )
        self.assertEqual(str(item), 'trainee: Person')


class TestDiet(TestCase):
    def test_calories_default_0(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.Diet.objects.create(
            trainee=trainee
        )
        self.assertEqual(item.calories, 0)

    def test_date_is_today(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.Diet.objects.create(
            trainee=trainee
        )
        today_date = date.today()
        self.assertEqual(item.created_date, today_date)

    def test_calories_ideal_default_0(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.Diet.objects.create(
            trainee=trainee
        )
        self.assertEqual(item.calories_ideal, 0)

    def test_calories_ideal_default_0(self):
        user = User.objects.create(username='tester', password='kjhasdf')
        trainee = models.TraineeInfo.objects.create(
            trainee=user,
            name='Person',
            age=30,
            weight=50,
            height=50
        )
        item = models.Diet.objects.create(
            trainee=trainee
        )
        self.assertEqual(str(item), 'This diet is for: Person')
