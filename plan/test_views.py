from django.test import TestCase
from django.test import Client
from django.urls import reverse
from . import models
from django.contrib.auth.models import User
    # def setUpTestData(cls):
    #     print("setUpTestData: Run once to set up non-modified data for all class methods.")
    #     pass


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
    return [user, item]


class TestHomeView(TestCase):
    def test_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_info_form(self):
        user = trainee_item()
        test_data = {'user': user[0],
                     'name': 'tester',
                     'age': 10,
                     'weight': 10,
                     'height': 10,
                     'sex': 'M',
                     'goal': 'WL'}
        
        response = self.client.post('/', test_data)


class TestWorkoutView(TestCase):
    def test_response(self):
        item = trainee_item()
        # self.client.get(f'/plan/{item.name}')
