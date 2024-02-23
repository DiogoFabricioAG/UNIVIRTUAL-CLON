from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Event
from .serializers import EventSerializer
from Notification.models import Notification
from User.models import User
@api_view(['POST'])
def create_event(request):
    user = User.objects.get(pk = request.user.id)
    event = Event.objects.create(user=user,title = request.data.get('title'),created_at  = request.data.get('created_at'),date_event  = request.data.get('date_event'),description = request.data.get('description'))
    serializer = EventSerializer(event)
    return JsonResponse({
        'message':'Event was created',
        'event':serializer.data
    },safe=False)
@api_view(['POST'])
def edit_event(request,pk):
    event = Event.objects.get(pk = pk)
    eventedited = request.data.get('event') 
    event.title = eventedited['title']
    event.date_event = eventedited['date_event']
    event.description = eventedited['description']
    event.save()
    return JsonResponse({'message':'Event Edited'})

@api_view(['GET'])
def get_my_events(request):
    user = User.objects.get(pk = request.user.id)
    events = Event.objects.filter(user= user)
    serializer = EventSerializer(events,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_event_by_id(request,pk):
    event = Event.objects.get(pk = pk)
    serializer = EventSerializer(event)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_my_events_from_date(request):
    user = User.objects.get(pk = request.user.id)
    query = request.query_params['date']
    date = Event.objects.filter(date_event = query,user=user) 
    serializer = EventSerializer(date,many = True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['DELETE'])
def delete_event(request,pk):
    event = Event.objects.get(pk = pk)
    event.delete()
    return JsonResponse({'message':'The event was deleted'})
