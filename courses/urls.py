
from django.urls import path
from .views import create_article, create_question, create_answer, create_quiz, create_question_in_quiz

urlpatterns = [
    
    path('create_article/', create_article, name='create_article'),
    path('create_question/', create_question, name='create_question'),
    path('create_answer/<int:question_id>', create_answer, name='create_answer'),
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('create_question_in_quiz/<int:quiz_id>', create_question_in_quiz, name='create_question_in_quiz'),
]
