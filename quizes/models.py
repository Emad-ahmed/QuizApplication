from msilib.schema import Class
from statistics import mode
from django.db import models

# Create your models here.

Diff_Choice = (
    ("easy", "easy"),
    ("medium", "medium"),
    ("hard", "hard"),
)


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(
        help_text="Required Score In percent")
    difficulty = models.CharField(max_length=6, choices=Diff_Choice)

    def __str__(self):
        return f"{self.name} - {self.topic}"

    def get_question(self):
        return self.question_set.all()

    class Meta:
        verbose_name_plural = "Quizes"
