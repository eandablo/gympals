from django.test import TestCase
from django.test import Client
from django.shortcuts import get_object_or_404, reverse
from . import models
from django.contrib.auth.models import User
from .decisions import DietGen


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

    def setUp(self):
        self.logged_in = self.client.login(
            username='testuser', password='yoyoyoyo')
        self.trainee = models.TraineeInfo(
            trainee=self.user, name="tester", age=23, weight=53,
            height=167, sex="F", goal="WL", calories=2000)
        self.trainee.save()

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
        self.assertRedirects(response, '/')


class UserViewsWorkoutRelated(TestCase, DietGen):
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

    def test_workoutview_updates_exercise_log(self):
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
        key_1 = 'sets' + log.identifier
        key_2 = 'reps' + log.identifier
        response = self.client.post(
            f'/update/{log.id}',
            {key_1: 3,
             key_2: 12})
        updated_log = models.WorkoutLog.objects.get(id=1)
        self.assertEqual(updated_log.sets_actual, 3)
        self.assertEqual(updated_log.reps_actual, 12)

    def test_wlogview_view(self):
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
        response = self.client.get(f'/workoutlogs/{self.trainee.name}/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logs_view.html')

    def test_dlogview_view(self):
        log = models.Diet.objects.create(
            trainee=self.trainee,
            calories=100,
            calories_ideal=100
        )
        response = self.client.get(f'/dietlogs/{self.trainee.name}/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logs_view.html')

    def test_updatedietlog_updates_calories(self):
        response = self.client.post(f'/dietupdate/{self.trainee.name}',
                                    {'diet_input': 1800})
        log = get_object_or_404(models.Diet, trainee=self.trainee)
        self.assertEqual(log.calories, 1800)
        self.assertRedirects(response, f'/dietlogs/{self.trainee.name}/1')


class AdminViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser(
            'admin_user', 'admin_user@gmail.com', '123456')
        cls.user.save()

    def setUp(self):
        self.logged_in = self.client.login(
            username='admin_user', password='123456')
        for i in range(4):
            self.exercise = models.Exercises.objects.create(
                name=str(i),
                muscle_group='BACK',
                calories_burnt=5
            )

    def test_editexercise_view(self):
        response = self.client.get('/edit_exercise/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exercise_edit.html')

    def test_editexercise_can_edit_item(self):
        response = self.client.post('/edit_exercise/1',
                                    {'name': 'push-up',
                                     'muscle_group': 'CHEST',
                                     'youtube_link': 'https://www.youtube.com',
                                     'level': 2,
                                     'calories_burnt': 10,
                                     'gender': 'M'})
        my_exercise = models.Exercises.objects.get(name='push-up')
        self.assertEqual(my_exercise.muscle_group, 'CHEST')
        self.assertEqual(my_exercise.youtube_link, 'https://www.youtube.com')
        self.assertEqual(my_exercise.level, 2)
        self.assertEqual(my_exercise.calories_burnt, 10)
        self.assertRedirects(response, reverse('catalog'),
                             fetch_redirect_response=False)

    def test_deleteexercise_deletes_and_redirects(self):
        num_before = models.Exercises.objects.all().count()
        response = self.client.post('/delete/1', {'delete_code': '0'})
        num_after = models.Exercises.objects.all().count()
        self.assertEqual(num_before, num_after + 1)
        for i in range(2, num_before + 1):
            item = models.Exercises.objects.get(id=i)
            self.assertEqual(item.name, str(i - 1))
        self.assertRedirects(response, reverse('catalog'),
                             fetch_redirect_response=False)

    def test_deleteexercise_rejects_wrong_code(self):
        num_before = models.Exercises.objects.all().count()
        response = self.client.post('/delete/1', {'delete_code': 'a'})
        num_after = models.Exercises.objects.all().count()
        self.assertEqual(num_before, num_after)
        self.assertRedirects(response, '/edit_exercise/1',
                             fetch_redirect_response=False)
