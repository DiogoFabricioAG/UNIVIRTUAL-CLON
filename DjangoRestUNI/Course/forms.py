from django import forms
from .models import CourseMaterial
from .serializers import CourseSerializer
class CourseMaterialForm(forms.ModelForm):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = CourseMaterial
        fields = ("name","materialtype",'course','link','file')
