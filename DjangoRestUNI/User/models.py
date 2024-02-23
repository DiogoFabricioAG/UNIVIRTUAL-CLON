from datetime import timedelta
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone 

from django.utils.timesince import timesince
class CustomUserManager(UserManager):
    def _create_user(self,authcode, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email = email, authcode = authcode, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_user(self, authcode = None, email = None,password = None, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(authcode,email,password,**extra_fields)
    
    def create_superuser(self, authcode = None, email = None , password = None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(authcode,email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    authcode = models.CharField(max_length=9,unique=True)
    email = models.EmailField(blank = True,default = '', unique = True) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    qrcode = models.ImageField(upload_to='qrcodes', blank=True, null=True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    description = models.TextField()
    friends = models.ManyToManyField('self',blank=True)
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True , null = True)
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default =True)
    STUDENT = 'Student'
    PROFFESOR = 'Professor'
    ADMINISTRATOR = 'Administrator'
    @property
    def name(self):
        return self.first_name.split()[0] +' '+self.last_name.split()[0]
    @property
    def date_joined_formatted(self):
        return timesince(self.date_joined)
    @property
    def last_login_formatted(self):
        return timesince(self.last_login+timedelta(hours=5))
    @property
    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        else:
            return 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/User-avatar.svg/120px-User-avatar.svg.png?20201213175635'
    
    @property
    def get_qr(self):
        if self.qrcode:
            return 'http://127.0.0.1:8000' + self.qrcode.url
    ROLE_CHOICES=(
        (ADMINISTRATOR,'Administrator'),
        (STUDENT,'Student'),
        (PROFFESOR,'Professor'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=15,default=STUDENT)
    objects = CustomUserManager()
    USERNAME_FIELD = 'authcode'
    REQUIRED_FIELDS = ['email','first_name', 'last_name']
    def __str__(self):
        return f'{self.role} {self.last_name}'
    @property
    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        else:
            return 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/User-avatar.svg/120px-User-avatar.svg.png?20201213175635'
        
class FriendshipRequest(models.Model):
    send_by = models.ForeignKey(User,related_name = 'friendshipsends',on_delete=models.CASCADE)
    send_to = models.ForeignKey(User,related_name = 'friendshiprequests',on_delete=models.CASCADE)
