from django.contrib import admin
from courses.models import Category, Article,Question,Answer,QuestionInQuiz,Quiz
# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionInQuiz)
admin.site.register(Quiz)