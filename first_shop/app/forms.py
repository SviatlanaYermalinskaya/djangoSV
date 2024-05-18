from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title', 'price', 'size', 'quantity', 'product_description', 'model_description', 'delivery_description',
            'vendor_code', 'category', 'gender')



