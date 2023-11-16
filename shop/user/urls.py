from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'user'


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="core:index"), name='logout'),
    path('register-success/', views.register_success, name='register_success'),
    path('load_cart/', views.LoadCart.as_view(), name='load_cart'),
   
]