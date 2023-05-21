from django.urls import path
from .views import order_create, OrderList, OrderUpdate


app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('order_list/', OrderList.as_view(), name='order_list'),
    path('order_update/<int:pk>/', OrderUpdate.as_view(), name='order_update'),
]