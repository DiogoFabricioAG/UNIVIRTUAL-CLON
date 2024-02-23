from django.db import models
import uuid
class College(models.Model): #Facultad
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=7)
    image = models.ImageField(upload_to='Facultades/',null=True)
    @property
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return 'https://portal.uni.edu.pe/images/logos/logo_uni_2016.png'
    def __str__(self):
        return self.short_name
class Career(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, related_name='careers', on_delete=models.CASCADE)
    @property
    def nstudent(self):
        return self.Users.filter(role='Student').count()
    @property
    def nproffesor(self):
        return self.Users.filter(role='Professor').count()

    def __str__(self):
        return self.name