from django.urls import path
from .views import CommandCreate, CommandDelete, Commands, PostDelete, PostDetail, PostUpdate, PrivacyPolicy, TextCallbacks, posts, PostCreate, TermsOfUse, CommandEdit, Main, TextCallbackView, Donate

urlpatterns = [
    path('', Main.as_view(), name='main_url'),
    path('posts', posts, name='post_list_url'),
    path('callback/create', TextCallbackView.as_view(), name='callback_url'),
    path('post/create', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('privacy_policy', PrivacyPolicy.as_view(), name='privacy_policy_url'),
    path('terms_of_use', TermsOfUse.as_view(), name='terms_of_use_url'),
    path('commands/create', CommandCreate.as_view(), name='command_create_url'),
    path('commands/<str:name>/update', CommandEdit.as_view(), name='command_update_url'),
    path('commands/<str:name>/delete', CommandDelete.as_view(), name='command_delete_url'),
    path('commands', Commands.as_view(), name='commands_url'),
    path('donate', Donate.as_view(), name='donate_url'),
    path('callbacks', TextCallbacks.as_view(), name='callbacks_url'),
    path('callbacks/<str:slug>/delete', TextCallbacks.as_view(), name='textcallback_delete_url')
]