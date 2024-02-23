import uuid
from django.db import models
from Career.models import Career 
from User.models import  User
from django.utils.timesince import timesince
class Course(models.Model):
    name = models.CharField(max_length=100)
    career = models.ManyToManyField(Career, related_name='courses_in')
    image = models.ImageField(upload_to='course', blank=True,null=True, max_length=None)
    code = models.CharField(max_length = 10)
    seccion = models.CharField(max_length=2)
    validation = models.CharField(blank = True, max_length = 10)
    active = models.BooleanField(default=True)
    @property
    def get_image(self):
        return 'http://127.0.0.1:8000' +self.image.url
    students = models.ManyToManyField(User, related_name='courses_students', blank=True)
    requirements = models.ManyToManyField('self',blank=True)
    professors = models.ManyToManyField(User, related_name='courses_teachers', blank=True)
    admin = models.ForeignKey(User, related_name="course_admin", on_delete=models.CASCADE, null=True,blank=True)
    solicitors = models.ManyToManyField(User, verbose_name="courses_solicitors",blank=True)
    def __str__(self) -> str:
        return self.name
    asynchronous = models.BooleanField(default=False)


class CourseMaterial(models.Model):
    NEWS='News'
    URLS='Urls'
    FIELDSPDF = 'PDF'
    FIELDSVIDEO = 'Videos'
    TEST = 'Test'
    TYPE_CHOICES = (
        (NEWS,'News'),
        (URLS,'Urls'),
        (FIELDSPDF , 'PDF'),
        (FIELDSVIDEO ,'Videos'),
        (TEST , 'Test'),
    )
    name = models.CharField(max_length=100)
    materialtype = models.CharField(choices = TYPE_CHOICES, default = FIELDSPDF,max_length = 10)
    course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
    link = models.URLField(max_length=200,blank=True)
    file = models.FileField(upload_to='course/materials',  blank=True,null=True ,max_length=100) # Mejorar el upload de los archivos colocar mas especificacion
    is_visible = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name + ' [' + self.course.name+ ']' 
    @property
    def get_file(self):
        if self.file:
            return 'http://127.0.0.1:8000' + self.file.url
    @property
    def get_link_embed(self):
        return self.link.replace('https://www.youtube.com/watch?v=','https://www.youtube.com/embed/')
    

class Report(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    created_by = models.ForeignKey(User, related_name="reportsfor", on_delete=models.CASCADE)
    created_for = models.ForeignKey(User, related_name="myreports", on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    reference_course = models.ForeignKey(Course,related_name = 'reports',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def created_at_formatted(self):
        return timesince(self.created_at)