from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class Workspace(models.Model):
    name =  models.CharField(max_length=100)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    desc = models.TextField()

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    workspace = models.ManyToManyField(Workspace, blank=True)


    def __str__(self):
        return self.username


    def get_workspace_values(self):
        ret = ''
        print(self.workspace.all())
    # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for i in self.workspace.all():
            ret = ret + i.name + ','
    # remove the last ',' and return the value.
        return ret[:-1]
    

class Doc(models.Model):
    doc_name = models.CharField(max_length=100)
    uploaded_by= models.ForeignKey(User, on_delete=models.CASCADE)
    doc = models.FileField()
    time_upload = models.DateTimeField(auto_now_add=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return self.doc



