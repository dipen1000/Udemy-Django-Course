from django.urls import path
from django.contrib.auth import views as authentication_views
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(http_method_names=["post", "get", "options"], template_name='users/logout.html'), name='logout'),
    path('profile/', views.profilePage, name='profile')
    
    
    # path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] 
