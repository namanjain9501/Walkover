from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    pass

# class doc(models.model):
#     name

class Doc(models.Model):
    doc_name = models.CharField(max_length=100)
    uploaded_by= models.ForeignKey(User, on_delete=models.CASCADE)
    doc = models.FileField()
    time_upload = models.DateTimeField(auto_now_add=True)


class Workspace(models.Model):
    name =  models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()