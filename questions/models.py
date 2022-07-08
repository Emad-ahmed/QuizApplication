from pyexpat import model
from tkinter.messagebox import QUESTION
from django.db import models
from quizes.models import Quiz

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answer(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question : {self.question.text}, answer : {self.text}, Correct : {self.correct}"
