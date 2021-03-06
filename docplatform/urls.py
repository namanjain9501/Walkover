from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('upload/<id>', views.upload, name="upload"),
    path('list/<id>', views.list, name="list"),
    path('content/<int:id_doc>/<int:id_work>/', views.content, name="content"),
    path('front/', views.front, name="front"),
    path('create/', views.create, name="create"),
    path('', views.test, name="test"),
    path('join/<id>', views.join, name="join"),
    path('welcome/<id>', views.welcome, name="welcome"),
    path('doc_list/<id>', views.doc_list, name="doc_list"),
    path('delete_doc/<int:id_doc>/<int:id_work>', views.delete_doc, name="delete_doc"),
    path('delete_workspace/<id>', views.delete_workspace, name="delete_workspace"),
]


