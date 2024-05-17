from django.contrib import admin

from .models import Category, ProductImage, Product, Order


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ProductImageInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'vendor_code')
    inlines = [ProductImageInline, ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'city', 'street_name')














