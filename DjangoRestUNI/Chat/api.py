from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import ChatMessage,ChatRoom
from .serializers import ChatMessageSerializer,ChatRoomSerializer
from Notification.models import Notification
from User.models import User
from User.serializers import UserSerializer
from Notification.models import Notification
from Course.models import Course

@api_view(['POST'])
def create_message(request,pk):
    send_to = ChatRoom.objects.get(pk = pk)
    send_by = User.objects.get(pk = request.user.id)
    try:
        message = ChatMessage.objects.create(send_to = send_to,send_by = send_by,content = request.POST['content'],image=request.FILES['image'])
    except: message = ChatMessage.objects.create(send_to = send_to,send_by = send_by,content = request.POST['content'])
    print(send_to.participants.all())
    for user in send_to.participants.all():
        if user != send_by:
            notification = Notification.objects.filter(send_by = send_by,send_to=user,typenotification='Received a Message')
            if notification.count() == 0 :
                Notification.objects.create(send_by = send_by,send_to=user,typenotification='Received a Message')
    serializer = ChatMessageSerializer(message)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def create_group(request):
    title = request.POST['title']
    image = request.FILES['file']
    user = User.objects.get(pk = request.user.id)
    myGroup = ChatRoom.objects.create(name=title,image=image,typeof = 'Group')
    myGroup.participants.add(user)
    myGroup.admins.add(user)
    myGroup.save()
    return JsonResponse({'message':'Creation was succesfull'})

@api_view(['POST'])
def create_chatroom(request,pk):
    myUser = User.objects.get(pk = request.user.id)
    otherUser = User.objects.get(pk = pk)
    if myUser == otherUser: return JsonResponse({'message':"Can't send a message to yourself"}) #Will be change
    if ChatRoom.objects.filter(typeof = 'Private', participants__in = [myUser]).filter(participants__in = [otherUser]).count() == 0:
        room = ChatRoom.objects.create(name = "Private " + myUser.name + " " +otherUser.name)
        room.participants.add(myUser)
        room.participants.add(otherUser)
        room.admins.add(myUser)
        room.admins.add(otherUser)
        room.save()
        return JsonResponse({'message':'Created'})
    else: 
        return JsonResponse({'message':'Already Exist'})

@api_view(['POST'])
def add_user_to_group(request,pk,id):
    room = ChatRoom.objects.get(pk = pk)
    user = User.objects.get(pk = id)
    room.participants.add(user)
    #Excepciones
    room.save()
    return JsonResponse({'message':'User was added to the group'})

@api_view(['POST'])
def create_message_for_a_forum(request,pk):
    forum = ChatRoom.objects.get(pk=pk)
    user = User.objects.get(pk = request.user.id)
    message = ChatMessage.objects.create(send_to = forum,send_by = user,content = request.data.get('content'),title = request.data.get('title'))
    return JsonResponse({
        'message':'Message was created',
        'obj': ChatMessageSerializer(message).data                
        },safe=False)

@api_view(['POST'])
def create_forum(request,pk):
    course = Course.objects.get(pk = pk)
    title = "Foro del curso " + course.name
    forum = ChatRoom.objects.create(name = title,typeof = 'Forum',image=course.image)
    for user in course.students.all():
        forum.participants.add(user)
    for user in course.professors.all():
        forum.participants.add(user)
    forum.save()
    return JsonResponse({'message':'Forum was created successfully'})

@api_view(['POST'])
def edit_group(request,pk):
    room = ChatRoom.objects.get(pk = pk)
    room.name = request.POST['name']
    try:
        room.image = request.FILES['image']
    except:pass
    if request.POST['admin'] != 'None':
        newadmin = User.objects.get(authcode = request.POST['admin'])
        if newadmin not in room.admins.all():
            room.admins.add(newadmin)
    room.save()
    return JsonResponse({'message':'ok'})


#GET
@api_view(['GET'])
def get_myforums(request):
    user = User.objects.get(pk = request.user.id)
    forum = ChatRoom.objects.filter(participants__in =[user],typeof = 'Forum')
    serializer =ChatRoomSerializer(forum,many=True)
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET'])
def get_all_groups_im_in(request):
    user = User.objects.get(pk = request.user.id)
    groups = ChatRoom.objects.filter(participants__in = [user])
    groups = groups.filter(typeof = 'Private') | groups.filter(typeof = 'Group')
    serializer = ChatRoomSerializer(groups,many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_messages_from_a_group(request,pk):
    send_to = ChatRoom.objects.get(pk = pk)
    messages = send_to.messages.all()
    user = User.objects.get(pk = request.user.id)
    if user in send_to.admins.all():
       state=True
    else: state=False
    serializer_group = ChatRoomSerializer(send_to)
    serializer = ChatMessageSerializer(messages,many=True)
    return JsonResponse({
        'messages':serializer.data,
        'group':serializer_group.data,
        'state':state
    },safe=  False)

@api_view(['GET'])
def get_forum_from_course(request,pk):
    course = Course.objects.get(pk = pk)
    forum = ChatRoom.objects.filter(typeof = 'Forum').filter(name__icontains=course.name)
    if forum.count():
        serializer = ChatRoomSerializer(forum,many=True)
        return JsonResponse(serializer.data,safe=False)
    else:
        return JsonResponse({'message':"This course doesn't have a forum"})

@api_view(['GET'])
def groups_im_admin(request):
    user = User.objects.get(pk = request.user.id)
    groups = ChatRoom.objects.filter(admins__in = [user]).filter(typeof = 'Group')
    serializer = ChatRoomSerializer(groups,many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_messages_from_a_forum(request,pk):
    forum = ChatRoom.objects.get(pk=pk)
    messages = forum.messages.all()
    serializer = ChatMessageSerializer(messages,many=True)
    return JsonResponse(serializer.data,safe=False)



@api_view(['GET'])
def get_chat_room(request,pk):
    room = ChatRoom.objects.get(pk = pk)
    serializer = ChatRoomSerializer(room)
    return JsonResponse(serializer.data,safe=False)


@api_view(['DELETE'])
def kickout_myself(request,pk):
    room = ChatRoom.objects.get(pk = pk)
    serializer = ChatRoomSerializer(room)
    user = User.objects.get(pk = request.user.id)
    room.participants.remove(user)
    if room.participants.count() == 0:
        room.delete()
        
        return JsonResponse({
            'message':'Group was deleted',
            'room':serializer.data        
        },safe=False)
    return JsonResponse({
        'message':'You left the group',
        'room':serializer.data 
        },safe=False)