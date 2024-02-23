from rest_framework import serializers
from .models import Notification
from User.serializers import UserSerializer
class NotificationSerializer(serializers.ModelSerializer):
    send_by = UserSerializer(read_only = True)
    send_to = UserSerializer(read_only = True)
    class Meta:
        model = Notification
        fields = ('id','typenotification','send_by','send_to','created_at_formatted','read_it','link')
