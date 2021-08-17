from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_and_reg),
    path('home', views.home),
    path('dashboard', views.dashboard),
    path('job', views.job),
    path('edit', views.edit),
    path('view', views.view),
]
