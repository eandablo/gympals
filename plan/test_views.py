from django.test import TestCase
from django.test import Client
from django.urls import reverse
from . import models
from django.contrib.auth.models import User
# def setUpTestData(cls):


class TestLogin(TestCase):
    def test_login(self):
        user = User.objects.create(username='testuser')
        user.set_password('yoyoyoyo')
        user.save()
        logged_in = self.client.login(username='testuser', password='yoyoyoyo')
        print(logged_in)
        print(user.is_authenticated)


class TestHomeView(TestCase):
    def test_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
