from django.urls import path
from .views import ProductListlView, ProductDetailView, CategoryListlView, \
    by_category, ProductAddView, contact, search


urlpatterns = [
    path('products', ProductListlView.as_view(), name='products'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('', CategoryListlView.as_view(), name='categories'),
    path('products/<int:category_id>/', by_category, name='by_category'),
    path('add', ProductAddView.as_view(), name='add'),
    path('cont', contact, name='contact'),
    path('search/', search, name='search'),
]

