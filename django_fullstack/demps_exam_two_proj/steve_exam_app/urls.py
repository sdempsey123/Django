from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.log_and_reg),
    path('login', views.login),
    path('register', views.register),
    path('home', views.home),
    path('logout', views.logout),
    path('wishes', views.wishes),
    path('stats', views.stats),
    path('new', views.new),
    path('edit', views.edit),
    path('new_wish', views.new_wish),
    path('grant', views.grant),
    path('update', views.update),
    path('delete', views.delete),
    path('like', views.like),
]
