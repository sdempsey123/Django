from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # This is where I get the first page seen when I run server.
    path('result', views.result), 
]