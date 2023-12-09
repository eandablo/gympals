from django.test import TestCase
from django.contrib.auth.models import User
from . import models
from .decisions import WorkoutGen, DietGen, workout_calories


class DecisionsTests(TestCase, WorkoutGen, DietGen):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('yoyoyoyo')
        cls.user.save()

    def setUp(self):
        self.logged_in = self.client.login(
            username='testuser', password='yoyoyoyo')
        self.trainee = models.TraineeInfo(
            trainee=self.user, name="tester", age=23, weight=53,
            height=167, sex="F", goal="WL", calories=2000)
        self.trainee.save()
        for i in range(4):
            self.exercise = models.Exercises.objects.create(
                name=str(i),
                muscle_group='BACK',
                calories_burnt=5
            )
        self.test_calc_set = [
            {'sex': 'F', 'goal': 'WL',
             'factor': 1.85, 'rest_s': -161, 'rest_w': -500},
            {'sex': 'F', 'goal': 'MG',
             'factor': 2.2, 'rest_s': -161, 'rest_w': 15},
            {'sex': 'F', 'goal': 'DF',
             'factor': 1.85, 'rest_s': -161, 'rest_w': 15},
            {'sex': 'M', 'goal': 'WL',
             'factor': 1.85, 'rest_s': 5, 'rest_w': -500},
            {'sex': 'M', 'goal': 'MG',
             'factor': 2.2, 'rest_s': 5, 'rest_w': 15},
            {'sex': 'M', 'goal': 'DF',
             'factor': 1.85,  'rest_s': 5, 'rest_w': 15},
            {'sex': 'N', 'goal': 'WL',
             'factor': 1.85, 'rest_s': -100, 'rest_w': -500},
            {'sex': 'N', 'goal': 'MG',
             'factor': 2.2, 'rest_s': -100, 'rest_w': 15},
            {'sex': 'N', 'goal': 'DF',
             'factor': 1.85, 'rest_s': -100, 'rest_w': 15}
        ]

    def test_select_ids(self):
        self.select_ids(self.trainee.name)
        logs = models.WorkoutLog.objects.filter(trainee=self.trainee)
        self.assertEqual(len(logs), 3)

    def test_workout_calories(self):
        self.select_ids(self.trainee.name)
        calories = workout_calories(self.trainee.name)
        self.assertEqual(
            calories,
            3 * models.Exercises.objects.get(id=1).calories_burnt)

    def test_calories_calc(self):
        weight = float(self.trainee.weight)
        height = float(self.trainee.height)
        age = float(self.trainee.age)
        self.select_ids(self.trainee.name)
        for item in self.test_calc_set:

            calories = self.calories_calc(self.trainee.name)
