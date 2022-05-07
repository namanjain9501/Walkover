from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('upload/', views.upload, name="upload"),
    path('list/<id>', views.list, name="list"),
    path('content/<id>', views.content, name="content"),
    path('front/', views.front, name="front"),
    path('create/', views.create, name="create"),
    path('', views.test, name="test"),
    path('join/<id>', views.join, name="join"),
]


