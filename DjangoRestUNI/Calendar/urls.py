from django.urls import path
from . import api

urlpatterns = [
    path('create-event/',api.create_event,name='create_event'),
    path('get-events/',api.get_my_events,name='get_my_events'),
    path('get-event/<int:pk>/',api.get_event_by_id,name='get_event_by_id'),
    path('get-events-date',api.get_my_events_from_date,name='get_my_events_from_date'),
    path('deleted-event/<int:pk>/',api.delete_event,name='delete_event'),
    path('edit-event/<int:pk>/',api.edit_event,name='edit_event'),

]
