
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.join, name ='join'),
    path('home/', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('login/', views.login, name='login'),

]
