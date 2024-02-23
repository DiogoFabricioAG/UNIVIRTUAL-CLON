from rest_framework import serializers
from .models import Blog,BlogPost,Like
from User.serializers import UserSerializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only = True)
    class Meta:
        model = Blog
        fields = ('id','owner','my_followers','public')

class BlogPostSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = ('id','blog','subject','body','visible','count_of_likes','created_at_formatted','get_image','get_file',)
