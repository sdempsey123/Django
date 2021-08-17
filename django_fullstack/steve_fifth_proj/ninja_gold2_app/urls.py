from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('process_money', views.process_money),
    # process_money was new route created in index.html, go to views file to create there
    path('reset', views.reset),
]