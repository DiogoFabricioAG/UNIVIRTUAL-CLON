from django.contrib import admin
from .models import  *

admin.site.register(Quiz)
admin.site.register(QuizProblem)
admin.site.register(QuizSolution)
admin.site.register(QuizUserSolution)
admin.site.register(UserResumeCourse) 