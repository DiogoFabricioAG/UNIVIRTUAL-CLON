from django.contrib import admin
from .models import Course,CourseMaterial
from User.models import User
from django import forms

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        students = User.objects.filter(role='Student')
        professors = User.objects.filter(role = 'Professor')
        admin = User.objects.filter(role = 'Professor')
        
        self.fields['students'].queryset = students
        self.fields['professors'].queryset = professors
        self.fields['admin'].queryset = admin

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = ['name', 'image', 'asynchronous','active']
    
admin.site.register(CourseMaterial)
   
