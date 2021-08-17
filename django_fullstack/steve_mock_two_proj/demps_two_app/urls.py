from django.urls import path
from .import views
urlpatterns = [
    path('', views.log_and_reg),
    path('register', views.register),
    # path('logout', views.logout),
    path('login', views.login),
    path('success', views.success),
    path('create_user', views.register),
    
]    