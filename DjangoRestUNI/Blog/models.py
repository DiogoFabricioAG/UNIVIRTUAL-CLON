from django.db import models
from User.models import User
from django.utils.timesince import timesince

class Blog(models.Model):
    owner = models.ForeignKey(User, related_name='blog', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(User,related_name='followers',blank=True)
    public = models.BooleanField(default = True)
    def __str__(self) -> str:
        return self.owner.name
    @property 
    def my_followers(self):
        return self.followers.count()
class Like(models.Model):
    created_by = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)


class BlogPost(models.Model):
    subject = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, related_name='posts',on_delete=models.CASCADE)
    body = models.TextField()
    visible = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment_file = models.ImageField(upload_to='postsimg', null=True,blank=True)
    file = models.FileField(upload_to='postsfile', max_length=100, null=True,blank=True)
    likes = models.ManyToManyField(Like, related_name='posts', blank = True)
    @property
    def get_image(self):
        if self.attachment_file:
            return 'http://127.0.0.1:8000' +self.attachment_file.url
        
    @property
    def get_file(self):
        if self.file:
            return 'http://127.0.0.1:8000' +self.file.url
    @property
    def created_at_formatted(self):
        return timesince(self.created_at)

    @property
    def count_of_likes(self):
        return self.likes.count()
   
    