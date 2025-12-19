from django.urls import path
from . import views_html

urlpatterns = [
    path('products/', views_html.product_list, name='product_list'),
    path('products/<int:pk>/', views_html.product_detail, name='product_detail'),
    path('products/create/', views_html.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views_html.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views_html.product_delete, name='product_delete'),
    path('categories/', views_html.category_list, name='category_list'),
]
