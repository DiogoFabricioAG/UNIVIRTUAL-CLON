from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *
from .models import *
from User.models import User
from User.serializers import UserSerializer


@api_view(['GET'])
def a_blog_exist(request,pk):
    user = User.objects.get(pk=pk)
    try:
        blog = Blog.objects.get(owner=user)
        return JsonResponse({'state':'yes'})
    except(Blog.DoesNotExist):
        return JsonResponse({'state':'no'})
    
@api_view(['POST'])    
def change_visibility_of_a_post(request,pk):
    post = BlogPost.objects.get(pk=pk)
    post.visible = not post.visible
    post.save()
    return JsonResponse({'message':'changed'})
@api_view(['GET'])
def get_blog(request,pk):
    user = User.objects.get(pk=pk)
    blog = Blog.objects.get(owner=user)
    serializer = BlogSerializer(blog)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def create_blog(request,pk):
    user = User.objects.get(pk=pk)
    blog = Blog.objects.create(owner=user,public = request.data.get('public'))
    return JsonResponse({'message':'yeh'})
    
@api_view(['POST'])
def follow_a_blog(request,pk):
    user = User.objects.get(pk = request.user.id)
    blog = Blog.objects.get(owner = User.objects.get(pk=pk))
    blog.followers.add(user)     
    return JsonResponse({'message':'follow'})

@api_view(['DELETE'])
def unfollow_a_blog(request,pk):
    user = User.objects.get(pk = request.user.id)
    blog = Blog.objects.get(owner = User.objects.get(pk=pk))
    blog.followers.remove(user)     
    return JsonResponse({'message':'unfollow'})

@api_view(['GET'])
def is_following(request,pk):
    user = User.objects.get(pk = request.user.id)
    blog = Blog.objects.get(owner = User.objects.get(pk=pk))
    is_following = blog.followers.filter(pk=user.pk).exists()

    return JsonResponse({'is_following': is_following})



@api_view(['GET'])
def get_posts(request,pk):
    user = User.objects.get(pk=pk)
    blog = Blog.objects.get(owner=user)
    #posts_blog = BlogPost.objects.filter(blog = blog)
    serializer = BlogPostSerializer(blog.posts.all(),many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def get_post(request,pk):
    post = BlogPost.objects.get(pk=pk)
    serializer = BlogPostSerializer(post)
    return JsonResponse(serializer.data,safe=False) 

@api_view(['DELETE'])
def destroy_that_blog(request,pk):
    user = User.objects.get(pk=pk)
    blog = Blog.objects.get(owner=user)
    blog.delete()
    return JsonResponse({'message':'destroy'})

@api_view(['GET'])
def like_was_already_given(request,pk):
    user = User.objects.get(id=request.user.id)
    post = BlogPost.objects.get(pk = pk)
    try:
        a = post.likes.get(created_by=user)
        return JsonResponse({'message':'True'})
    except:
        if post.likes.filter(created_by = user).count()>1: return JsonResponse({'message':'True'}) 
        return JsonResponse({'message':'False'}) 

@api_view(['POST'])
def create_post(request,pk):
    user = User.objects.get(pk=pk)
    blog = Blog.objects.get(owner=user)
    valuebool = True
    if request.POST['visible'] == 'true': valuebool = True
    else: valuebool = False
    if request.POST['type']=='None':
        blogpost = BlogPost.objects.create(subject = request.POST['subject'],blog=blog,body = request.POST['body'],visible = valuebool) # Utilizar Forms Genericos
    elif request.POST['type']=='Imagen':
        blogpost = BlogPost.objects.create(subject = request.POST['subject'],blog=blog,body = request.POST['body'],attachment_file=request.FILES['archivo'],visible = valuebool) # Utilizar Forms Genericos
    else:
        blogpost = BlogPost.objects.create(subject = request.POST['subject'],blog=blog,body = request.POST['body'],file=request.FILES['archivo'],visible = valuebool) # Utilizar Forms Genericos
    
    return JsonResponse({'message':'success'})
    #form = CourseMaterialForm(request.post)

@api_view(['POST'])
def edit_post(request,pk):
    post = BlogPost.objects.get(pk=pk)
    if request.POST['visible'] == 'true': valuebool = True
    else: valuebool = False
    post.subject = request.POST['subject']
    post.body = request.POST['body']
    post.visible = valuebool
    if request.POST['type']=='None':
        pass
    elif request.POST['type']=='Imagen':
        post.attachment_file = request.FILES['archivo']
    else :
        post.file = request.FILES['archivo']    
    post.save()
    return JsonResponse({'message':'success'})


@api_view(['DELETE'])
def delete_post(request,pk):
    post = BlogPost.objects.get(pk = pk)
    post.delete()
    return JsonResponse({'message':'deleted'})



@api_view(['POST'])
def create_like(request,pk):
    user = User.objects.get(id=request.user.id)
    post = BlogPost.objects.get(pk = pk)
    post.likes.create(created_by=user)
    return JsonResponse({'message':'Like was GIVEN'})


@api_view(['DELETE'])
def destroy_like(request,pk):
    user = User.objects.get(id=request.user.id)
    post = BlogPost.objects.get(pk = pk)
    like = post.likes.filter(created_by = user)[0]
    for i in post.likes.all():
        if i.created_by == like.created_by:
            post.likes.remove(i)
    return JsonResponse({'message':'Like was DESTROY'})
