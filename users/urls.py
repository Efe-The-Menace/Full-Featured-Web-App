from django.urls import path
from django.contrib.auth import views
from . import views as user_views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.user_profile, name='profile'),
    path('profile/update/', user_views.profile_edit, name='profile_edit')
]