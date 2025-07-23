from django.urls import path, reverse_lazy
from django.contrib.auth import views
from . import views as user_views
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetDoneView,
    PasswordResetView,
    PasswordResetConfirmView
)

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/ ', user_views.user_profile, name='profile'),
    path('profile/update/', user_views.profile_edit, name='profile_edit'),
    
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset.html'
             ),
         name='password_reset'),
    
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
             ),
         name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
             ),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html',
             ),
         name='password_reset_complete')
]