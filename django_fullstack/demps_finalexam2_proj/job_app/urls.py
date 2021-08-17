from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.log_and_reg),
    path('register', views.register),
    path('login', views.login),
    path('jobs', views.jobs),
    # path('job', views.job),
    path('dashboard', views.dashboard),
    path('jobs/create', views.create),
    path('edit', views.edit, name='edit'),
    path('jobs/new', views.new),
    path('dashboard/<int:job_id>/edit', views.edit),
    path('edit/<int:user_id>/update', views.update, name='update_user'),
    # path('jobs/update', views.update),
#     path('<int:job_id>/update', views.update),
]