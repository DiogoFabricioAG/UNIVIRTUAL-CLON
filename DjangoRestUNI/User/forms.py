from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('authcode','email','country','city','description','role','first_name','last_name','password1','password2')
