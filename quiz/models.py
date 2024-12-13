from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

class QuizSession(models.Model):
    session_id = models.CharField(max_length=36)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_correctly = models.BooleanField()
