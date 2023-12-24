from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Article, Question, Answer, Quiz, QuestionInQuiz
from .forms import ArticleForm, QuestionForm, AnswerForm, QuizForm, QuestionInQuizForm

def index(request):
    context ={
        'key1':'value1',
        'key2': 'value2',
    }
    return render(request, 'courses/index.html', context)

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.teacher = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'courses/create_article.html', {'form': form})

@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.student = request.user
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'courses/create_question.html', {'form': form})

@login_required
def create_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.teacher = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'courses/create_answer.html', {'form': form, 'question': question})

@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.teacher = request.user
            quiz.save()
            return redirect('quiz_detail', pk=quiz.pk)
    else:
        form = QuizForm()
    return render(request, 'courses/create_quiz.html', {'form': form})

@login_required
def create_question_in_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        form = QuestionInQuizForm(request.POST)
        if form.is_valid():
            question_in_quiz = form.save(commit=False)
            question_in_quiz.quiz = quiz
            question_in_quiz.save()
            return redirect('quiz_detail', pk=quiz.pk)
    else:
        form = QuestionInQuizForm()
    return render(request, 'courses/create_question_in_quiz.html', {'form': form, 'quiz': quiz})
