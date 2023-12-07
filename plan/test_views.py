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
        self.assertEqual(trainee.name, "tester")
        self.assertEqual(trainee.name, "tester")
        self.assertEqual(trainee.name, "tester")


class TestWorkoutView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('yoyoyoyo')
        cls.user.save()
        for i in range(4):
            print(i)
            cls.exercise = models.Exercises.objects.create(
                name=str(i),
                muscle_group='BACK',
                calories_burnt=5
            )
    # name = models.CharField(max_length=150, unique=True)
    # guide_image = CloudinaryField('image', default='None')
    # muscle_group = models.CharField(max_length=10, choices=GROUPS)
    # youtube_link = models.CharField(max_length=200, unique=True,
    #                                 default='None')
    # level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    # calories_burnt = models.PositiveIntegerField(default=0)
    # gender = models.CharField(max_length=1, choices=GENDERS, default='B')


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

    def test_workoutview_response(self):
        print(self.trainee)