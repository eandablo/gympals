from django.test import TestCase
from django.test import Client
from django.shortcuts import get_object_or_404, reverse
from . import models
from django.contrib.auth.models import User
from trainer import settings
# def setUpTestData(cls):


class TestSignup(TestCase):
    def test_signup_view(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_user_signup(self):
        response = self.client.post(
            reverse('account_signup'),
            {"username": 'testuser',
             "password": 'yoyoyoyo'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')


class TestLogin(TestCase):
    def test_login_view(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_user(self):
        user = User.objects.create(username='testuser')
        user.set_password('yoyoyoyo')
        user.save()
        logged_in = self.client.login(username='testuser', password='yoyoyoyo')
        self.assertTrue(logged_in)


class TestHomeView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('yoyoyoyo')
        cls.user.save()

    def test_home_view(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_post(self):
        logged_in = self.client.login(username='testuser', password='yoyoyoyo')
        self.client.post('/',
                         {"name": "tester",
                          "age": 23,
                          "weight": 53,
                          "height": 167,
                          "sex": "F",
                          "goal": "WL"})
        trainee = get_object_or_404(models.TraineeInfo, trainee=self.user)
        self.assertEqual(trainee.trainee, self.user)
        self.assertEqual(trainee.age, 23)
        self.assertEqual(trainee.weight, 53)
        self.assertEqual(trainee.height, 167)
        self.assertEqual(trainee.sex, "F")
        self.assertEqual(trainee.goal, "WL")


class UpdateInfoView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('yoyoyoyo')
        cls.user.save()
        for i in range(4):
            cls.exercise = models.Exercises.objects.create(
                name=str(i),
                muscle_group='BACK',
                calories_burnt=5
            )

    def setUp(self):
        self.logged_in = self.client.login(
            username='testuser', password='yoyoyoyo')
        self.client.post('/',
                         {"name": "tester",
                          "age": 23,
                          "weight": 53,
                          "height": 167,
                          "sex": "F",
                          "goal": "WL"})
        self.trainee = get_object_or_404(models.TraineeInfo, trainee=self.user)

    def test_info_is_updated(self):
        response = self.client.post(f'/info/{self.trainee.name}',
                                    {"age": 24,
                                     "weight": 54,
                                     "height": 168,
                                     "goal": "MG"})
        trainee_updated = get_object_or_404(
            models.TraineeInfo, trainee=self.user)
        self.assertEqual(trainee_updated.age, 24)
        self.assertEqual(trainee_updated.weight, 54)
        self.assertEqual(trainee_updated.height, 168)
        self.assertEqual(trainee_updated.goal, "MG")


class LogWorkoutView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('yoyoyoyo')
        cls.user.save()
        for i in range(4):
            cls.exercise = models.Exercises.objects.create(
                name=str(i),
                muscle_group='BACK',
                calories_burnt=5
            )

    def setUp(self):
        self.logged_in = self.client.login(
            username='testuser', password='yoyoyoyo')
        self.client.post('/',
                         {"name": "tester",
                          "age": 23,
                          "weight": 53,
                          "height": 167,
                          "sex": "F",
                          "goal": "WL"})
        self.trainee = get_object_or_404(models.TraineeInfo, trainee=self.user)

    def test_workoutview_post(self):
        my_exercise = get_object_or_404(models.Exercises, id=1)
        log = models.WorkoutLog.objects.create(
            identifier='week1',
            day=1,
            trainee=self.trainee,
            sets_ideal=3,
            reps_ideal=12,
            completed=False,
            excercise=my_exercise
        )
        response = self.client.post(f'/update/{log.id}',
                                    {'sets_actual': 3,
                                     'reps_actual': 12})
        updated_log = models.WorkoutLog.objects.get(id=1)
        self.assertEqual(updated_log.sets_actual, 3)
        self.assertEqual(updated_log.reps_actual, 12)
