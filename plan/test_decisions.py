from django.test import TestCase
from django.contrib.auth.models import User
from . import models
from .decisions import WorkoutGen


class DecisionsTests(TestCase, WorkoutGen):
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

    def test_select_ids(self):
        self.select_ids(self.trainee.name)
        