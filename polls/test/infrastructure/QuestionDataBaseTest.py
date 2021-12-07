import datetime

from django.test import TestCase

from polls.infrastructure.models.models import Question


class AnimalTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="lion", pub_date=datetime.datetime.now())

    def test_animals_can_speak(self):
        question = Question.objects.get(question_text="lion")
        field_label = question._meta.get_field('question_text').verbose_name
        self.assertEqual(field_label, 'question text')

    def test_first_name_max_length(self):
        question = Question.objects.get(question_text="lion")
        max_length = question._meta.get_field('question_text').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Question.objects.get(question_text="lion")
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)
