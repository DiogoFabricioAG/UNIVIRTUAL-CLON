from django.urls import path
from . import api  

urlpatterns = [
    path('<uuid:pk>/',api.get_blog,name='get_blog'),
    path('<uuid:pk>/create/',api.create_blog,name='create_blog'),
    path('<uuid:pk>/follow/',api.follow_a_blog,name='follow_a_blog'),
    path('<uuid:pk>/unfollow/',api.unfollow_a_blog,name='unfollow_a_blog'),
    path('<uuid:pk>/isfollowing/',api.is_following,name='is_following'),
    path('<uuid:pk>/destroy/',api.destroy_that_blog,name='destroy_that_blog'),
    path('<uuid:pk>/exist/',api.a_blog_exist,name='a_blog_exist'),
    path('<uuid:pk>/posts/',api.get_posts,name='get_posts'),
    path('<uuid:pk>/posts/create/',api.create_post,name='create_post'),
    path('posts/delete/<int:pk>/',api.delete_post,name='delete_post'),
    path('post/<int:pk>/',api.get_post,name='get_post'),
    path('post/<int:pk>/change/',api.change_visibility_of_a_post,name='change_visibility_of_a_post'),
    path('post/<int:pk>/edit/',api.edit_post,name='edit_post'),
    path('like/<int:pk>/create/',api.create_like,name='create_like'),
    path('like/<int:pk>/delete/',api.destroy_like,name='destroy_like'),
    path('like/<int:pk>/was-given/',api.like_was_already_given,name='like_was_already_given'),
]
