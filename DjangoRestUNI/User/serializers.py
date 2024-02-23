from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User,FriendshipRequest
from Career.serializers import CareerSerializer

class UserSerializer(serializers.ModelSerializer):
    career = CareerSerializer(read_only =True)
    class Meta:
        model = User
        fields=('id','authcode','name','email','get_avatar','first_name','get_qr','last_name','role','description','date_joined_formatted','last_login_formatted','country',
                'city','career')
        def validate_password(self, value: str) -> str:
            return make_password(value)

class FriendshipRequestSerializer(serializers.ModelSerializer):
    send_by = UserSerializer(read_only =True)
    send_to = UserSerializer(read_only =True)
    class Meta:
        model = FriendshipRequest
        fields = ('id','send_by','send_to')