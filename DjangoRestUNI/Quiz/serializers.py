from rest_framework import serializers
from .models import Quiz,QuizProblem,QuizSolution,QuizUserSolution,UserResumeCourse
from Course.serializers import CourseSerializer
from User.serializers import UserSerializer
class QuizSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Quiz
        fields = ('id','course','total_points','attempts','problems','state','solutions','title','typeoftest','time')
class QuizProblemSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = QuizProblem
        fields = ('id','title','content','points','quiz',)
class QuizSolutionSerializer(serializers.ModelSerializer):
    problem = QuizProblemSerializer(read_only=True)
    class Meta:
        model = QuizSolution
        fields = ('id','is_correct','problem','content')

class QuizUserSolutionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only = True)
    user = UserSerializer(read_only = True)
    class Meta: 
        model = QuizUserSolution
        fields = ('id','quiz','user','created_at_formatted','qualification')
class UserResumeCourseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only  = True)
    course = CourseSerializer(read_only  = True)
    class Meta: 
        model = UserResumeCourse
        fields = ('id','course','user','grade_prom','passed','get_certificate')
