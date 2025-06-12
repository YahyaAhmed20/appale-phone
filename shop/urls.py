from django.urls import path, include
from . import views



app_name = 'shop'
urlpatterns = [
    path('', views.shop_list, name='shop_list'),  # URL for the job list view
  

]