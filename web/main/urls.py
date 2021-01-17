from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_works', views.my_works, name='my_works'),
    path('login', views.login, name='login'),
    path('create', views.create, name='create'),
]