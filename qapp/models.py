from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.answer