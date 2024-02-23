from .models import Event
from rest_framework import serializers
from User.serializers import UserSerializer

class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Event
        fields = ('id','title','description','user','created_at','date_event')