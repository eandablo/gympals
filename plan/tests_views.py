from django.test import TestCase


class TestHome(TestCase):
    def test_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
