from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/list/', views.ProductListView.as_view(), name='products_list'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('product/instance/<int:pk>/', views.ProductDetailView.as_view(), name='product_instance'),
]
