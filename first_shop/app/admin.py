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
    list_filter = ('gender', 'category')
    search_fields = ('title__icontains', 'vendor_code')
    inlines = [ProductImageInline, ]
    date_hierarchy = 'created'
    fields = ['title', ('price', 'quantity', 'size'), ('vendor_code', 'category', 'gender'), 'product_description',
              'model_description', 'delivery_description']
    search_help_text = 'Введите название или артикул товара'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'city', 'street_name')
