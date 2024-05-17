from django.urls import path

from app import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.index, name='index'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('product/instance/<int:pk>/', views.product_instance, name='product_instance'),
]
