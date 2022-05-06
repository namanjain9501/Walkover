from django.contrib import admin
from . models import Doc, User, Workspace
# Register your models here.
admin.site.register(User)
admin.site.register(Doc)
admin.site.register(Workspace)


