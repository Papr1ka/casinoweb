from django.urls import path
from .views import PostDelete, PostDetail, PostUpdate, PrivacyPolicy, posts, PostCreate

urlpatterns = [
    path('', posts, name='post_list_url'),
    path('post/create', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('privacy_policy', PrivacyPolicy.as_view(), name='privacy_policy_url'),
]