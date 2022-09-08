import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text =models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    # Metodo que nos devuelve el output.
    def __str__(self):
        return self.question_text

    # Metodo para saber si la pregunta fue publicada recientemente.
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str(self):
        return self.choice_text
