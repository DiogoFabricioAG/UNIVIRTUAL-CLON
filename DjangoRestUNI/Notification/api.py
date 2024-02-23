from .serializers import NotificationSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Notification
from User.models import User

@api_view(['GET'])
def get_all_my_notifications(request):
    user = User.objects.get(pk = request.user.id)
    notification = Notification.objects.filter(send_to = user)
    serializer = NotificationSerializer(notification,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def get_one_notification(request,pk):
    notification = Notification.objects.get(pk = pk)
    serializer = NotificationSerializer(notification)
    notification.read_it = True
    notification.save()
    return JsonResponse(serializer.data,safe=False)

@api_view(['DELETE'])
def destroy_a_notification(request,pk):
    notification = Notification.objects.get(pk = pk)
    notification.delete()
    return JsonResponse({'message':'Notification was deleted successfully'})