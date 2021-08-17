from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.log_and_reg),
    path('register', views.register),
    path('shows/', views.shows),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>', views.show),
    # path('dashboard', views.dashboard),
    # localhost:8000/shows
    
    # localhost:8000/shows/new
    path('shows/new', views.new),
    # localhost:8000/shows/create
    path('shows/create', views.create),
    # localhost:8000/shows/<show_id>/edit
    # path('<int:show_id>/edit', views.edit),
    # localhost:8000/shows/<show_id>/update
    # path('<int:show_id>/update', views.update),
    # localhost:8000/shows/<show_id>
    # localhost:8000/shows/<show_id>/delete
    path('<int:show_id>/delete', views.delete),
    path('logout', views.logout),
    path('login', views.login),
    # path('success', views.success),
]