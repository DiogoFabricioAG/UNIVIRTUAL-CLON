from django.contrib import admin
from .models import ChatMessage,ChatRoom

admin.site.register(ChatRoom)
admin.site.register(ChatMessage)