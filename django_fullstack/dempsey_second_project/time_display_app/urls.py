from django.urls import path     
from . import views
# app_name = 'timedisplay'
urlpatterns = [
    path('', views.index),
    # path('date', views.date),
    # path('string', views.string),
    path('home', views.home),
]

