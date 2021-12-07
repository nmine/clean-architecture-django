from django.test import TestCase


class TestCalls(TestCase):
    def test_call_view_deny_anonymous(self):
        response = self.client.get('/polls', follow=True)
        self.assertRedirects(response, '/login/')
