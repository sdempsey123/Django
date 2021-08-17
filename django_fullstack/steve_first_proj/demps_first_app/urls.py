from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000
    path('', views.index),
    # localhost:8000/new
    path('new', views.new),
    path('create', views.create),
    # path('create', views.create),
    path('show/<str:name>', views.person),
    # I was able to run with http://127.0.0.1:8000/show/name
    path('edit/<str:number>', views.steve),
    path('destroy', views.destroy),
]




