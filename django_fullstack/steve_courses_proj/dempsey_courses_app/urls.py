from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    path('', views.index),
    # path('course', views.course),
    path('delete', views.delete),
    path('course/add', views.add),
    path('<int:destroy_id>/destroy', views.destroy),
    path('<int:comments_id>/comments', views.comments),
    path('comment', views.comment),
    
]


