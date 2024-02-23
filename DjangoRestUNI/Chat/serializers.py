from rest_framework import serializers
from .models import ChatMessage,ChatRoom
from User.serializers import UserSerializer
class ChatRoomSerializer(serializers.ModelSerializer):
    
    participants = UserSerializer(read_only = True, many = True)
    admins = UserSerializer(read_only = True,many = True)
    
    class Meta:
        model = ChatRoom
        fields = ('id','participants','name','count_users','count_messages','get_image','admins','typeof')
    
class ChatMessageSerializer(serializers.ModelSerializer):
    
    send_to = ChatRoomSerializer(read_only = True)
    send_by = UserSerializer(read_only = True)
    
    class Meta:
        model = ChatMessage
        fields = ('id','send_to','send_by','title','content','created_at_formatted','get_image')
