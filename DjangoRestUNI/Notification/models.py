import uuid
from django.db import models
from User.models import User
from django.utils.timesince import timesince
class Notification(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    typenotification = models.CharField(max_length=25)
    send_by = models.ForeignKey(User, related_name='notifications_sended', on_delete=models.CASCADE,null=True,blank = True)
    send_to = models.ForeignKey(User, related_name='notifications_receive', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    read_it = models.BooleanField(default = False)
    link = models.URLField(max_length=255,blank=True,null=True)
    @property
    def created_at_formatted(self):
        return timesince(self.created_at)