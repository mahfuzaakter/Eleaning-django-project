from django.db import models

# Create your models here.
# from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class QuestionInQuiz(models.Model):
    question = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
