from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from Calendar import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('colleges/',include('Career.urls')),
    path('course/',include('Course.urls')),
    path('blog/',include('Blog.urls')),
    path('quiz/',include('Quiz.urls')), 
    path('chat/',include('Chat.urls')),
    path('notification/',include('Notification.urls')),
    path('calendar/',include('Calendar.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
