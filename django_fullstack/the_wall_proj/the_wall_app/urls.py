from django.urls import include, path
from . import views

urlpatterns =[
    # path('', views.index),
    path('', views.log_and_reg),
    path('wall', views.wall),
    path('profile', views.profile),
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    # path('message', views.message),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('delete_message' , views.delete_message),
    path('delete_comment', views.delete_comment),
    

    
]
