from . import api   

from django.urls import path

urlpatterns = [
    path('createfor/<int:pk>/',api.create_quiz,name='create_quiz'),
    path('quizzesfrom/<int:pk>/',api.get_the_quizes_from_a_course,name='get_the_quizes_from_a_course'),
    path('<uuid:pk>/',api.get_quiz_by_id,name='get_quiz_by_id'),
    path('<uuid:pk>/send/',api.create_user_response_for_a_quiz,name='create_user_response_for_a_quiz'),
    path('<uuid:pk>/create_problem/',api.set_problems_for_a_quiz,name='set_problems_for_a_quiz'),
    path('<uuid:pk>/available/',api.set_available,name='set_available'),
    path('<uuid:pk>/problems/',api.get_problems_from_a_quiz,name='get_problems_from_a_quiz'),
    path('problem/<int:pk>/',api.get_solutions,name='get_solutions'),
    path('myquizes/<int:pk>/',api.get_users_solutions,name='get_users_solutions'),
    path('myquizes/attempts/<uuid:pk>/',api.get_my_attempts,name='get_my_attempts'),
    path('finish/<int:pk>/',api.set_finish_course,name='set_finish_course'),
    path('myresumes/',api.get_resume,name='get_resume'),
    path('delete/<uuid:pk>/',api.destroy_quiz,name='destroy_quiz'),
]
