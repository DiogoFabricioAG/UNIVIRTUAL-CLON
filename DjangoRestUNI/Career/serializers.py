from rest_framework import serializers
from .models import Career,College
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields=('id','name','short_name','get_image')


class CareerSerializer(serializers.ModelSerializer):
    college = CollegeSerializer(read_only =True)
    class Meta:
        model = Career
        fields=('id','name','college')
