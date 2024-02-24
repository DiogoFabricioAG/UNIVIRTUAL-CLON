from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer,FriendshipRequestSerializer
from .models import User,FriendshipRequest
from datetime import datetime
from django.core.files.base import ContentFile
from . import utils
from .forms import SignupForm
from django.contrib.auth.forms import PasswordChangeForm
from Notification.models import Notification
@api_view(['GET'])
def me(request):
    user = User.objects.get(pk = request.user.id)
    user.last_login = datetime.now()
    user.save()
    return JsonResponse({
        'id': request.user.id,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'role': request.user.role,
        #'get_avatar' : request.user.get_avatar,
    })

@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many = True)
    return JsonResponse(serializer.data,safe=False) 

@api_view(['GET'])
def get_user_by_id(request,pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data,safe=False) 

@api_view(['POST'])
def edit_user(request,pk):
    user = User.objects.get(pk=pk)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.country = request.POST['country']
    user.city = request.POST['city']
    try:
        user.avatar = request.FILES['avatar']
    except:
        pass
    user.save()
    return JsonResponse({'message':'success'})

@api_view(['GET'])
def get_requests(request):
    user = User.objects.get(pk = request.user.id)
    myrequests = FriendshipRequest.objects.filter(send_to = user)
    serializer = FriendshipRequestSerializer(myrequests,many = True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def send_friendshiprequest(request):
    user = User.objects.get(pk = request.data.get('id'))
    usersend = User.objects.get(pk = request.user.id)



    if FriendshipRequest.objects.filter(send_by = usersend, send_to = user).count() !=0 or FriendshipRequest.objects.filter(send_by = user, send_to = usersend).count() !=0:
        return JsonResponse({'message':'There is a friendship request whit this user.'})
    elif usersend in user.friends.all():
        return JsonResponse({'message':'This user is already your friend.'})
    elif user == usersend:
        return JsonResponse({'message':"Cant't send a request to yourself"})
    else:
        FriendshipRequest.objects.create(send_to = user,send_by=usersend)
        Notification.objects.create(send_to=user,send_by=usersend,typenotification = f'El usuario "{usersend.name}" te ha mandado una solicitud de amistad.')

        return JsonResponse({'message':'Friendship request was sended succesfully.'})

@api_view(['POST'])
def friendshiprequest_options(request,option):
    user = User.objects.get(pk = request.user.id)
    userfrom = User.objects.get(pk = request.data.get('id'))
    friendrequest =  FriendshipRequest.objects.get(send_to = user,send_by = userfrom)
    # 0 ACCEPTED
    # 1 DENIED
    if option:
        message = 'The request was denied'
    else:
        user.friends.add(userfrom)
        userfrom.friends.add(user)
        message = 'The request was accepted'
    friendrequest.delete()
    return JsonResponse({'message':message})

@api_view(['POST'])
def password_change(request):
    user = User.objects.get(pk = request.user.id)
    form = PasswordChangeForm(user = user,data = request.POST)
    error = ''
    message='success'
    if form.is_valid():
        form.save()
    else:
        message = 'NOT GOOD'
        error= form.errors
    return JsonResponse({
        'message':message,
        'error': error,
        },safe=False)

@api_view(['GET'])
def get_list_of_friends(request):
    user = User.objects.get(pk = request.user.id)
    friends = user.friends.all()
    serializer = UserSerializer(friends,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['DELETE'])
def delete_friend(request,pk):
    user = User.objects.get(pk = request.user.id)
    friend = User.objects.get(pk = pk)
    user.friends.remove(friend)
    friend.friends.remove(user)
    return JsonResponse({'message':'Deleted'})
@api_view(['POST'])
def generate_qr(request, pk):
    user = User.objects.get(pk=pk)
    url = request.data.get('url') 
    if url:
        qr_image = utils.create_qr_code('http://localhost:5173' + url['fullPath'])
        user.qrcode.save('qrcode.png', ContentFile(qr_image), save=True)
        return JsonResponse({
            'message': 'QR code generated and saved',
            'url_image':user.get_qr
            }, safe=False)
    else:
        return JsonResponse({'error': 'URL not provided in request'}, status=400)
    
@api_view(['POST'])    
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    error = ''
    message = 'User creation was ok'
    form = SignupForm({
        'email':      data.get('email'),
        'authcode':   data.get('authcode'),
        'country':    data.get('country'),
        'city':        data.get('city'),
        'description': data.get('description'),
        'role':        data.get('role'),
        'last_name':   data.get('last_name'),
        'first_name': data.get('first_name'),
        'password1':   data.get('password1'),
        'password2':   data.get('password2'),
    })
    if form.is_valid():
        user = form.save()
        user.save()
    else:
        error= form.errors
        message= 'User creation was wrong'
    return JsonResponse({
        'message':message,
        'error': error,
        },safe=False)