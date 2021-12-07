from django.core.mail.backends import console
from django.test import TestCase
import datetime
from polls.infrastructure.models.models import Question


class AnimalTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="lion", pub_date=datetime.datetime.now())

    def test_animals_can_speak(self):
        question = Question.objects.get(question_text="lion")
