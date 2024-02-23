from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import CollegeSerializer,CareerSerializer
from .models import College,Career

@api_view(['GET']) 
def get_colleges(request):
    colleges = College.objects.all()
    serializer = CollegeSerializer(colleges,many =True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_college_by_id(request,pk):

    college = College.objects.get(pk=pk)
    serializer = CollegeSerializer(college)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_all_careers(request):
    serializer = CareerSerializer(Career.objects.all(),many=True)
    return JsonResponse(serializer.data,safe=False)


