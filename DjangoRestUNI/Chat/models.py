from django.db import models
import uuid
from User.models import User
from datetime import timedelta
class ChatRoom(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 255)
    participants = models.ManyToManyField(User,related_name='groups_in')
    admins = models.ManyToManyField(User,related_name="admin_of")
    typeof = models.CharField(max_length = 25, default = 'Private')
    image = models.ImageField(upload_to='groups', blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    
    
    @property
    def count_messages(self):
        return self.messages.count()

    @property
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' +self.image.url
        else:
            return None
    @property
    def count_users(self):
        return self.participants.count()

class ChatMessage(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    send_to = models.ForeignKey(ChatRoom,related_name = 'messages',on_delete = models.CASCADE)
    send_by = models.ForeignKey(User,related_name = 'my_messages',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length =100, blank=True,null=True)
    content = models.TextField() 
    image = models.ImageField(upload_to='Chat/images', blank=True,null=True)
    
    @property
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' +self.image.url
        else: return False

    @property
    def created_at_formatted(self):
        time = self.created_at -timedelta(hours=5)
        return time.strftime('%Y/%m/%d %H:%M:%S')