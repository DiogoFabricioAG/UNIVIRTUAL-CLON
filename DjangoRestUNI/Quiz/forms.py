from django import forms
from .models import Quiz
from .serializers import CourseSerializer


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('problems','title','attempts','solutions','typeoftest','time')
