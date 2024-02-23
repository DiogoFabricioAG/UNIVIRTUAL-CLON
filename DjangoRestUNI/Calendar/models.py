from django.db import models
from User.models import User
class Event(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    date_event = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)