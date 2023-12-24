from django import forms
from .models import Article, Question, Answer, Quiz, QuestionInQuiz

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content', 'article']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'question']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'category']

class QuestionInQuizForm(forms.ModelForm):
    class Meta:
        model = QuestionInQuiz
        fields = ['question']
