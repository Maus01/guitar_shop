from django.urls import path

from . import views

app_name = 'cart'


urlpatterns = [
    path('add/', views.cart_add, name='cart_add'),
    path('summary/', views.cart_summary, name='cart_summary'),
    path('update', views.cart_update, name='cart_update'),
    path('delete', views.cart_delete, name='cart_delete'),
    
]