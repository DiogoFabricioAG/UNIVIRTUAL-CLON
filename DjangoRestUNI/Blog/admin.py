from django.contrib import admin
from .models import Blog,BlogPost,Like

admin.site.register(Blog)
admin.site.register(BlogPost)
admin.site.register(Like)