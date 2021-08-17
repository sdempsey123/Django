from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.log_and_reg),
    path('register', views.register),
    path('books', views.books),
    path('logout', views.logout),
    path('login', views.login),
    # path('success', views.success),
    path('books/create', views.create),
    path('books/<int:book_id>', views.book_profile),
    path('books/<int:book_id>/update', views.update),
    path('books/<int:book_id>/delete', views.delete),
    path('books/<int:book_id>/unfavorite', views.unfavorite),
    path('books/<int:book_id>/favorite', views.favorite),
]