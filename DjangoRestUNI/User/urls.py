from . import api   
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

urlpatterns = [
    path('',api.get_user,name='users'),
    path('<uuid:pk>/',api.get_user_by_id,name='user_by_id'),
    path('me/',api.me,name='me'),
    path('signup/',api.signup,name='signup'),
    path('friends/',api.get_list_of_friends,name='get_list_of_friends'),
    path('friends/delete/<uuid:pk>/',api.delete_friend,name='delete_friend'),
    path('edit/<uuid:pk>/',api.edit_user,name='edit_user'),
    path('login/',TokenObtainPairView.as_view(), name='token_obtain'),
    path('editpassword/',api.password_change, name='password_change'),
    path('generate-qr/<uuid:pk>/',api.generate_qr, name='generate_qr'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('myrequests/',api.get_requests,name='get_requests'),
    path('sendrequest/',api.send_friendshiprequest,name='send_friendshiprequest'),
    path('friendship-request-options/<int:option>/',api.friendshiprequest_options,name='friendshiprequest_options'),
] 
 