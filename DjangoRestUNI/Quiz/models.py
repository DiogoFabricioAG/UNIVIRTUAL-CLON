from django.db import models
import uuid
from Course.models import Course
from User.models import User
from datetime import timedelta
class Quiz(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course,related_name='quizzes',on_delete = models.CASCADE,null=True)
    problems = models.IntegerField()
    solutions = models.IntegerField(default=4)
    attempts = models.IntegerField(default = 1)
    state = models.CharField(max_length = 25, default = 'Not Available')
    NON_QUALIFIED = 'Quick (NON Q)'
    PRACTICE = 'Practice (PC)'
    PARCIAL = 'Parcial (EP)'
    FINAL = 'Final (EF)'
    SUSTITUTORY = 'Sustitutorio (ES)'
    
    QUIZ_CHOICE = (
        (NON_QUALIFIED , 'Quick (NON Q)'),
        (PRACTICE, 'Practice (PC)'),
        (PARCIAL ,'Parcial (EP)'),
        (FINAL ,'Final (EF)'),
        (SUSTITUTORY ,'Sustitutorio (ES)'),
    )

    typeoftest = models.CharField(choices=QUIZ_CHOICE, default = NON_QUALIFIED,max_length=20)
    time = models.DurationField()
    @property
    def total_points(self):
        total = 0
        for i in self.quizproblems.all():
            total+=i.points
        return total
    def __str__(self) -> str:
        return self.title

class QuizProblem(models.Model): 
    quiz = models.ForeignKey(Quiz,related_name='quizproblems',on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    points=models.IntegerField()
    def __str__(self) -> str:
        return self.quiz.title + ' Problem: ' + self.title

class QuizSolution(models.Model):
    problem = models.ForeignKey(QuizProblem, related_name='problem_solutions',on_delete = models.CASCADE)
    content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.problem.title + ' Solution: ' +self.content


class QuizUserSolution(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    quiz = models.ForeignKey(Quiz,related_name='users',on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name = 'quizzes',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    qualification = models.IntegerField()
    @property
    def created_at_formatted(self):
        time = self.created_at -timedelta(hours=5)
        return time.strftime('%Y/%m/%d %H:%M:%S')

class UserResumeCourse(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    course = models.ForeignKey(Course, related_name='resumes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='resumes', on_delete=models.CASCADE)
    grade_prom = models.IntegerField()
    passed = models.BooleanField()
    certificate = models.FileField(upload_to='Certificates',blank=True,null=True)
    
    @property
    def get_certificate(self):
        if self.certificate:
            return 'http://127.0.0.1:8000' +self.certificate.url
    
    def __str__(self) -> str:
        return 'Final '+ self.course.name +' for '+self.user.name