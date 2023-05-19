from django.urls import path
from .views import order_create, OrderList


app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('order_list/', OrderList.as_view(), name='order_list'),
]