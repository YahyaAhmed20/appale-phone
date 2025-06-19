from django.urls import path, include
from . import views



app_name = 'shop'
urlpatterns = [
    path('', views.shop_list, name='shop_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),

    path('<str:slug>/', views.shop_detail, name='shop_detail'),
]