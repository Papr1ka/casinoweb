from django.urls import path
from .views import posts, post

urlpatterns = [
    path('', posts, name='post_list'),
    path('post/<str:slug>/', post, name='post_list'),
]