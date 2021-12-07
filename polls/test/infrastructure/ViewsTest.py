import json

from django.test import TestCase


class TestCalls(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, "Hello, world. You're at the polls index.")
