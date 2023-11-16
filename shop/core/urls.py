from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug_category>', views.category, name='category'),
    path('product/<slug:slug_product>', views.product_detail, name='product_detail'),
    path('session/', views.session, name='session'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete/', views.complete_order, name='complete_order'),
    path('history/', views.history_list, name='history'),
    path('order_detail/<int:id>', views.order_detail, name='order_detail'),
    
]