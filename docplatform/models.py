from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class Workspace(models.Model):
    name =  models.CharField(max_length=100)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    desc = models.TextField()
    

class User(AbstractUser):
    workspace = models.ManyToManyField(Workspace, blank=True)
    

class Doc(models.Model):
    doc_name = models.CharField(max_length=100)
    uploaded_by= models.ForeignKey(User, on_delete=models.CASCADE)
    doc = models.FileField()
    time_upload = models.DateTimeField(auto_now_add=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)



