from . import api   

from django.urls import path

urlpatterns = [
    path('',api.get_courses,name='courses'),
    path('create/',api.create_course,name='create_course'),
    path('college/<uuid:pk>/',api.get_courses_from_college,name='get_courses_from_college'),
    path('users/<uuid:pk>/in',api.get_course_im_in,name='get_course_im_in'),
    path('<int:pk>/',api.get_course_by_id,name='course_by_id'),
    path('<int:pk>/set-code/',api.set_code_of_course,name='set_code_of_course'),
    path('<int:pk>/validate-code/',api.validate_enroll,name='validate_enroll'),
    path('<int:pk>/verifyuser/',api.user_is_in_a_course,name='user_is_in_a_course'),
    path('<int:pk>/users/',api.get_users_from_course,name='get_users_from_course'),
    path('<int:pk>/materials/',api.get_materials_from_course,name='get_materials_from_course'),
    path('<int:pk>/create_material/',api.create_course_material,name='create_course_material'),
    path('material/<int:pk>/',api.get_course_material,name='get_course_material'),
    path('material/<int:pk>/edit/',api.edit_course_material,name='edit_course_material'),
    path('material/<int:pk>/delete/',api.delete_course_material,name='delete_course_material'),
    path('material/<int:pk>/visibility/',api.set_visibility,name='set_visibility'),
    path('report/create/<uuid:pk>/course/<int:id>/',api.create_report,name='create_report'),
    path('report/',api.get_reports_for_me,name='get_reports_for_me'),
    path('forumexist/<int:pk>/',api.a_forum_exist,name='a_forum_exist'),
    path('opencourse/<int:pk>/',api.create_notification_for_a_opening,name='create_notification_for_a_opening'),
    path('setavailable/<int:pk>/',api.set_available_a_course,name='set_available_a_course'),
    path('<int:pk>/addsolicitor/',api.add_solicitors,name='add_solicitors'),
    path('<int:pk>/sendcode/',api.send_code_to_solicitors,name='send_code_to_solicitors'),
]
