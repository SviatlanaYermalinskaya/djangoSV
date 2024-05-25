from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/list', views.ProductListView.as_view(), name='products_list'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/instance/<int:pk>/', views.ProductDetailView.as_view(), name='product_instance'),
    path('order/create/<int:pk>/', views.order_create, name='order_create'),
]
