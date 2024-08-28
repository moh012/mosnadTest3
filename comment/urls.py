from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('userdata', views.userdata, name='userdata'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('pro', views.pro, name='pro'),
    path('pro_s/<int:id>', views.pro_s, name='pro_s'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('change_password/',
         auth_views.PasswordChangeView.as_view(
             template_name='pages/change_password.html'),
         name='change_password'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='pages/password_change_done.html'),
         name='password_change_done'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="pages/password_reset_form.html"),
         name='reset_password'),
    path('reset_password_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="pages/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="pages/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="pages/password_reset_complete.html"),
         name='password_reset_complete'),
]