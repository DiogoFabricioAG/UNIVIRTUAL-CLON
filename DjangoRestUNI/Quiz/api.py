from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import QuizForm
from .models import Quiz,QuizProblem,QuizSolution,QuizUserSolution,UserResumeCourse
from Notification.models import Notification
from Course.models import Course
from User.models import User
from .serializers import QuizSerializer,QuizProblemSerializer,QuizSolutionSerializer,QuizUserSolutionSerializer,UserResumeCourseSerializer

from . import utils
@api_view(['POST'])
def create_quiz(request,pk):
    form = QuizForm(request.POST)
    if form.is_valid():
        quiz= form.save(commit=False)
        quiz.course = Course.objects.get(pk=pk)
        quiz.save() 
        return JsonResponse({'message':'Saved'})
    return JsonResponse({'message':'An error has occurred'})

@api_view(['GET'])
def get_my_attempts(request,pk):
    quiz = Quiz.objects.get(pk =pk )
    user = User.objects.get(pk = request.user.id)
    my_attempts = QuizUserSolution.objects.filter(user=user,quiz= quiz)
    serializer =QuizUserSolutionSerializer(my_attempts,many=True)

    return JsonResponse(serializer.data,safe=False)

@api_view(['Delete'])
def destroy_quiz(request,pk):
    quiz = Quiz.objects.get(pk = pk)
    quiz.delete()
    return JsonResponse({
        'message':'Ok',
    },safe=False)

@api_view(['GET'])
def get_the_quizes_from_a_course(request,pk):
    course = Course.objects.get(pk = pk)
    quiz = course.quizzes.all()
    serializer = QuizSerializer(quiz,many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_users_solutions(request,pk):
    user = User.objects.get(pk = request.user.id)
    course = Course.objects.get(pk = pk)
    quiz = Quiz.objects.filter(course = course)
    practices = QuizUserSolution.objects.filter(user = user, quiz__in = quiz)
    serializer = QuizUserSolutionSerializer(practices,many= True)
    return JsonResponse(serializer.data,safe=False)
    
@api_view(['POST'])
def set_finish_course(request,pk):
    course = Course.objects.get(pk = pk)
    students = course.students.all()
    for student in students:
        utils.set_final_grades(student.id,course.id)
    course.active = False
    course.students.clear()
    course.save()
    return JsonResponse({'message':'Finish'})

@api_view(['GET'])
def get_quiz_by_id(request,pk):
    quiz = Quiz.objects.get(pk = pk) 
    serializer = QuizSerializer(quiz)
    return JsonResponse(serializer.data,safe=False)


@api_view(['POST'])
def set_problems_for_a_quiz(request,pk):
    quiz = Quiz.objects.get(pk = pk)
    problem = QuizProblem.objects.create(
        quiz = quiz,
        title = request.data.get('title'),
        content = request.data.get('content'),
        points = request.data.get('points'),
    )   
    for i in range(len(request.data.get('solutionscontext'))):
        try:
            is_correct = request.data.get('corrections')[i]
        except: is_correct = False
        QuizSolution.objects.create(
            problem = problem,
            content = request.data.get('solutionscontext')[i],
            is_correct = is_correct,
        )
    return JsonResponse({'message':'Created'})

@api_view(['PATCH'])
def set_available(request,pk):
    quiz = Quiz.objects.get(pk = pk)
    quiz.state = 'Available'
    quiz.save()
    for student in quiz.course.students.all():
        Notification.objects.create(send_to = student,typenotification='Quiz Available in: '+quiz.course.name)
    return JsonResponse({'message':"It's available"})

@api_view(['GET'])
def get_problems_from_a_quiz(request,pk):
    quiz = Quiz.objects.get(pk = pk)
    problems = quiz.quizproblems.all()
    serializer_problems =  QuizProblemSerializer(problems,many=True)
    return JsonResponse({
        'problems': serializer_problems.data,
    },safe=False)
@api_view(['GET'])
def get_solutions(request,pk):
    problem = QuizProblem.objects.get(pk = pk)
    solutions = problem.problem_solutions.all()
    serializer = QuizSolutionSerializer(solutions,many=True)
    return JsonResponse(serializer.data,safe=False)
    

@api_view(['POST'])
def create_user_response_for_a_quiz(request,pk):
    user = User.objects.get(pk = request.user.id)
    quiz = Quiz.objects.get(pk = pk)
    list_of_answers = request.data.get('answers')
    ids = request.data.get('ids')

    qualification = 0
    print(list_of_answers)
    print(ids)
    for index,answer in enumerate(list_of_answers):
        try:
            solution = QuizSolution.objects.get(pk = int(ids[index]))
            if solution.is_correct:
                qualification += solution.problem.points
        except:pass
    QuizUserSolution.objects.create(
        user = user,
        quiz = quiz,
        qualification = qualification,
    )

    return JsonResponse({'message':'given'})

@api_view(['GET'])
def get_resume(request):
    user = User.objects.get(pk = request.user.id)
    myResumes = UserResumeCourse.objects.filter(user=user)
    serializer = UserResumeCourseSerializer(myResumes,many=True)
    return JsonResponse(serializer.data,safe=False)