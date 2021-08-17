from django.urls import include, path
from . import views

urlpatterns =[
    # path('', views.index),
    path('', views.log_and_reg),
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    path('wall', views.wall),
    path('post_message', views.post_message),
    path('post_comment/<int:wall_message_id>', views.post_comment),
    path('delete_message/<int:wall_message_id>' , views.delete_message),
    path('delete_comment/<int:comment_id>', views.delete_comment),
    path('profile/<int:profile_id>', views.profile),

    
]
