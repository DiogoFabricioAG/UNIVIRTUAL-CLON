from rest_framework import serializers 
from .models import Course,CourseMaterial,Report
from User.serializers import UserSerializer
class CourseSerializer(serializers.ModelSerializer):
    students = UserSerializer(read_only = True, many=True)
    professors =  UserSerializer(read_only = True, many=True)
    admin = UserSerializer(read_only = True)
    class Meta:
        model = Course
        fields = ('id','name','get_image','active','code','validation','seccion','students','professors','admin','asynchronous')
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = ('id','name','materialtype','get_link_embed','get_file','link','is_visible')
class ReportSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only = True)
    created_for = UserSerializer(read_only = True)
    reference_course = CourseSerializer(read_only = True)
    class Meta:
        model = Report
        fields = ('id','created_by','created_for','title','content','reference_course','created_at_formatted')