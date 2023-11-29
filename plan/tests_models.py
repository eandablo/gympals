from django.test import TestCase
from . import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from datetime import date


def trainee_item():
    '''
    defining item for use in TestTraineeInfo
    '''
    user = User.objects.create(username='tester', password='kjhasdf')
    item = models.TraineeInfo.objects.create(
        trainee=user,
        name='Person',
        age=30,
        weight=50,
        height=50
    )
    return item


class TestTraineeInfo(TestCase):
    def test_sex_field_defaults_N(self):
        self.assertEqual(trainee_item().sex, 'N')

    def test_date_updates(self):
        date_today = date.today()
        self.assertEqual(trainee_item().updated_date, date_today)

    def test_goal_field_defaults_WL(self):
        self.assertEqual(trainee_item().goal, 'WL')

    def test_str_method_returns_name(self):
        self.assertEqual(str(trainee_item()), 'Person')


def exercise_item():
    '''
    defining item for use in TestExercises
    '''
    item = models.Exercises.objects.create(
        name='Test',
        muscle_group='BACK'
    )
    return item


class TestExercises(TestCase):
    def test_guide_image_defaults_none(self):
        self.assertEqual(exercise_item().guide_image, 'None')

    def test_image_link_defaults_none(self):
        self.assertEqual(exercise_item().youtube_link, 'None')

    def test_level_defaults_1(self):
        self.assertEqual(exercise_item().level, 1)

    def test_calories_burnt_defaults_0(self):
        self.assertEqual(exercise_item().calories_burnt, 0)

    def test_gender_defaults_N(self):
        self.assertEqual(exercise_item().gender, 'B')

    def test_str_method_returns_name(self):
        self.assertEqual(str(exercise_item()), 'exercise: Test')


def workoutlog_item():
    '''
    defining item for use in TestWorkoutLog
    '''
    exercise = models.Exercises.objects.create(
        name='Test',
        muscle_group='BACK'
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
    return item


class TestWorkoutLog(TestCase):
    def test_day_defaults_1(self):
        self.assertEqual(workoutlog_item().day, 1)

    def test_created_date_is_today(self):
        date_today = date.today()
        self.assertEqual(workoutlog_item().created_date, date_today)

    def test_logged_date_is_today(self):
        date_today = date.today()
        self.assertEqual(workoutlog_item().logged_date, date_today)

    def test_sets_ideal_defaults_0(self):
        self.assertEqual(workoutlog_item().sets_ideal, 0)

    def test_sets_actual_defaults_0(self):
        self.assertEqual(workoutlog_item().sets_actual, 0)

    def test_reps_ideal_defaults_0(self):
        self.assertEqual(workoutlog_item().reps_ideal, 0)

    def test_reps_actual_defaults_0(self):
        self.assertEqual(workoutlog_item().reps_actual, 0)

    def test_completed_defaults_False(self):
        self.assertFalse(workoutlog_item().completed)

    def test_string_returns_trainee_name(self):
        self.assertEqual(str(workoutlog_item()), 'trainee: Person')


def diet_item():
    '''
    defining item for use in TestDiet
    '''
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
    return item


class TestDiet(TestCase):
    def test_calories_default_0(self):
        self.assertEqual(diet_item().calories, 0)

    def test_date_is_today(self):
        date_today = date.today()
        self.assertEqual(diet_item().created_date, date_today)

    def test_calories_ideal_default_0(self):
        self.assertEqual(diet_item().calories_ideal, 0)

    def test_calories_ideal_default_0(self):
        self.assertEqual(str(diet_item()), 'This diet is for: Person')
