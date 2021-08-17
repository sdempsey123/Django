from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_page)
    path('python'), views.python_page)
]