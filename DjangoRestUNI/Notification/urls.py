from django.urls import path
from . import api
urlpatterns = [
    path('mynotifications/',api.get_all_my_notifications,name='get_all_my_notifications'),
    path('mynotifications/<uuid:pk>/',api.get_one_notification,name='get_one_notification'),
    path('mynotifications/<uuid:pk>/destroy/',api.destroy_a_notification,name='destroy_a_notification'),
]
