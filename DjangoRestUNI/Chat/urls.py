from django.urls import path
from . import api   
urlpatterns = [
    path('connection/<uuid:pk>/',api.create_message, name='create_message'),
    path('room/<uuid:pk>/',api.get_chat_room, name='get_chat_room'),
    path('room/<uuid:pk>/edited/',api.edit_group, name='edit_group'),
    path('room/<uuid:pk>/left/',api.kickout_myself, name='kickout_myself'),
    path('mygroups/',api.get_all_groups_im_in, name='get_all_groups_im_in'),
    path('myforums/',api.get_myforums, name='get_myforums'),
    path('myadmingroups/',api.groups_im_admin, name='groups_im_admin'),
    path('creategroups/',api.create_group, name='create_group'),
    path('messages/<uuid:pk>/',api.get_messages_from_a_group, name='get_messages_from_a_group'),
    path('private/<uuid:pk>/',api.create_chatroom, name='create_chatroom'),
    path('group/<uuid:pk>/add/<uuid:id>/',api.add_user_to_group, name='add_user_to_group'),
    path('forum/<int:pk>/',api.get_forum_from_course, name='get_forum_from_course'),
    path('forum/<int:pk>/create/',api.create_forum, name='create_forum'),
    path('forum/<uuid:pk>/createmessages/',api.create_message_for_a_forum, name='create_message_for_a_forum'),
    path('forum/<uuid:pk>/messages/',api.get_messages_from_a_forum, name='get_messages_from_a_forum'),
]
