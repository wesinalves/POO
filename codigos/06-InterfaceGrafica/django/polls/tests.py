from django.test import TestCase

# Create your tests here.
import datetime
from django.test import TestCase
from django.utils import timezone
from django.shortcuts import reverse

from .models import Question

def create_question(text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=time)

class QuestionModelsTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

class QuestionIndexViewTests(TestCase):
    def test_no_quesion(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Não há nenhuma questão")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    
    def test_past_question(self):
        question = create_question("past question", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question]
        )

    def test_future_question(self):
        create_question("future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Não há nenhuma questão")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])