from . import api   
from django.urls import path

urlpatterns = [
    path('all/',api.get_colleges,name='get_colleges'),
    path('<uuid:pk>/',api.get_college_by_id,name='get_college_by_id'),
    path('allcareers/',api.get_all_careers,name='get_all_careers'),
]
