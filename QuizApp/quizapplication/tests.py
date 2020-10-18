from django.test import TestCase
from quizapplication.models import Quiz, Question, Options, Student

class ModelTest(TestCase):

    def setUp(self):
        print("Setting up UT")
        tmp_text = "Physics Test-5"
        self.quiz = Quiz.objects.create(id=999, text=tmp_text)
        self.quiz = Quiz.objects.create(id=1000, text="Java Test-7")

    def test_add_quiz(self):
        print("test add quiz running.")
        tmp_text = "Chemistry Test-78"
        q = Quiz.objects.create(text=tmp_text)
        obj = Quiz.objects.get(id=q.id)
        self.assertEqual(obj.text, tmp_text)

    def test_add_quiz_neg(self):
        print("test add quiz running negative.")
        tmp_text = "Chemistry Test-79"
        q = Quiz.objects.create(text=tmp_text)
        obj = Quiz.objects.get(id=q.id)
        self.assertNotEquals(obj.text, tmp_text+"1234")

    def test_add_question(self):
        print("test add question running.")
        q_text = "Which Programming language JVM associated with?"
        q = Question.objects.create(text=q_text, Quiz_id= 1000)
        obj = Question.objects.get(id=q.id)
        self.assertEqual(str(obj.text), q_text)


