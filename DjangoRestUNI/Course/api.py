from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from User.serializers import UserSerializer
from .serializers import CourseSerializer,MaterialSerializer, ReportSerializer
from .models import Course,CourseMaterial,Report
from User.models import User
from . import utils
from Career.models import College,Career
from Notification.models import Notification
from Chat.models import ChatRoom
@api_view(['GET'])
def get_courses(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course,many=True)
    return JsonResponse(serializer.data,safe=False) 

@api_view(['GET'])
def a_forum_exist(request,pk):
    course = Course.objects.get(pk = pk)
    forum = ChatRoom.objects.filter(name = "Foro del curso " + course.name).filter(typeof = 'Forum')
    if forum.count() != 0:
        return JsonResponse({'status':True})
    else:
        return JsonResponse({'status':False})
@api_view(['GET'])
def get_course_by_id(request,pk):
    course = Course.objects.get(pk=pk)
    if course:
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data,safe=False) 
    else:
        return JsonResponse({"message':'This course doesn't exist!"})

@api_view(['POST'])
def create_course(request):
    career = Career.objects.get(name = request.POST['career'])
    user = User.objects.get(pk = request.user.id)
    course = Course.objects.create(name=request.POST['name'],code=request.POST['code'],seccion = request.POST['seccion'],image=request.FILES['image'])
    course.career.add(career)
    course.professors.add(user)
    course.admin = user
    course.save()
    return JsonResponse({'message':'Created'})
@api_view(['POST'])
def get_courses_from_college(request,pk):

    college = College.objects.get(pk = pk)
    if request.data['query']:

        courses = Course.objects.filter(career__in = college.careers.all()).filter(name__icontains = request.data['query'])
    else:
        courses = Course.objects.filter(career__in = college.careers.all())
    serializer = CourseSerializer(set(courses),many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_solicitors(request,pk):
    course =Course.objects.get(pk = pk)
    user = User.objects.get(pk = request.user.id)
    course.solicitors.add(user)
    course.save()
    return JsonResponse({'message':'Your solicitude was sended'})

@api_view(['POST'])
def set_available_a_course(request,pk):
    course = Course.objects.get(pk =pk)
    course.active = True
    course.save()
    return JsonResponse({'message':'Course was activated successfully'})

@api_view(['POST'])
def create_notification_for_a_opening(request,pk):
    course = Course.objects.get(pk =pk)
    user = User.objects.get(pk = request.user.id)
    for professor in course.professors.all():
        Notification.objects.create(send_by = user, send_to = professor, typenotification = f'El alumno {user.name} solicita la apertura del curso {course.name}')
    return JsonResponse({'message':'Requests was sended'})


@api_view(['GET'])
def user_is_in_a_course(request,pk):
    course = Course.objects.get(pk = pk)
    user = User.objects.get(pk = request.user.id ) 
    if request.user.role == 'Student':
        if user in course.students.all():
            return JsonResponse({'state':True})
    else:
        if user in course.professors.all():
            return JsonResponse({'state':True})
    return JsonResponse({'state':False})

@api_view(['GET'])
def get_course_im_in(request,pk):
    user = User.objects.get(pk=pk)
    courses = []
    if user.role == 'Student': 
        for i in Course.objects.filter(active = True):
            if user in i.students.all():
                courses.append(i)
    else: 
        for i in Course.objects.all():
            if user in i.professors.all():
                courses.append(i)
    
    serializer = CourseSerializer(courses,many=True)
    return JsonResponse(serializer.data,safe=False) 

@api_view(['GET'])
def get_materials_from_course(request,pk):
    course = Course.objects.get(pk=pk)
    material = course.materials.all()
    serializer = MaterialSerializer(material,many=True)
    return JsonResponse(serializer.data,safe=False) 


@api_view(['GET'])
def get_course_material(request,pk):
    material = CourseMaterial.objects.get(pk = pk)
    serializer = MaterialSerializer(material)
    return JsonResponse(serializer.data,safe=False) 

@api_view(['GET'])
def get_users_from_course(request,pk):
    course = Course.objects.get(pk = pk)
    users = []
    for i in course.students.all():
        users.append(i)
    for i in course.professors.all():
        users.append(i)
    serializer = UserSerializer(users,many =True)
    return JsonResponse(serializer.data,safe=False) 

@api_view(['GET'])
def get_reports_for_me(request):
    user = User.objects.get(pk = request.user.id)
    reports = Report.objects.filter(created_for = user)
    serializer = ReportSerializer(reports,many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def create_report(request,pk,id):
    teacher = User.objects.get(pk = request.user.id)
    user = User.objects.get(pk = pk)
    course = Course.objects.get(pk = id)
    Report.objects.create(created_by=teacher,created_for=user,title= request.data.get('title'),content= request.data.get('content'),reference_course=course)
    Notification.objects.create(send_to=user,send_by = teacher,typenotification='A Report was created for the course: '+course.name)
    return JsonResponse({'message':'Report was created'})

@api_view(['POST'])
def set_visibility(request,pk):
    material = CourseMaterial.objects.get(pk = pk)
    if material.is_visible:  material.is_visible = False
    else: material.is_visible = True
    material.save()
    return JsonResponse({'message':'success'},safe=False)

@api_view(['POST'])
def validate_enroll(request,pk):
    course = Course.objects.get(pk = pk)
    user = User.objects.get(pk = request.user.id) 
    if course.validation == request.POST['validation']:
        utils.add_new_member(user,course)
        return JsonResponse({'message':'Enrollment was successful'})
    else:
        return JsonResponse({'message':'Incorrect code of validation'})

@api_view(['POST'])
def send_code_to_solicitors(request,pk):
    course = Course.objects.get(pk = pk)
    for solicitor in course.solicitors.all():
        Notification.objects.create(send_to = solicitor,typenotification=f'El curso {course.name} tiene como codigo: {course.validation}')
    return JsonResponse({'message':'The Code was sended for notification for all the applicants'})

@api_view(['POST'])
def set_code_of_course(request,pk):
    course = Course.objects.get(pk = pk)
    course.validation = request.POST['validation']
    course.save()
    return JsonResponse({'message':'The code has been configured successfully.'})    

@api_view(['POST'])
def create_course_material(request,pk):
    try:
        material =CourseMaterial.objects.create(name = request.POST['name'],materialtype = request.POST['materialtype'],link = request.POST['link'],file = request.FILES['file'],
                                            course = Course.objects.get(pk= pk)) # Utilizar Forms Genericos
        return JsonResponse({'message':'success'})
    except:
        material =CourseMaterial.objects.create(name = request.POST['name'],materialtype = request.POST['materialtype'],link = request.POST['link'],
                                            course = Course.objects.get(pk= pk)) # Utilizar Forms Genericos
        return JsonResponse({'message':'success'})
    #form = CourseMaterialForm(request.post)


@api_view(['POST'])
def edit_course_material(request,pk):
    material = CourseMaterial.objects.get(pk = pk)
    material.name = request.POST['name']
    material.materialtype = request.POST['materialtype']
    material.link = request.POST['link']
    try:
        material.file = request.FILES['file']
    except:pass
    material.save()
    return JsonResponse({'message':'success'})

@api_view(['DELETE'])
def delete_course_material(request,pk):
    material = CourseMaterial.objects.get(pk = pk)
    material.delete()
    return JsonResponse({'message':'delete was successfull'})