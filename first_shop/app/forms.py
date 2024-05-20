from django import forms
from django.forms import inlineformset_factory

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title', 'price', 'size', 'quantity', 'product_description', 'model_description', 'delivery_description',
            'vendor_code', 'category', 'gender')


ProductImagesFormSet = inlineformset_factory(Product, ProductImage, fields='__all__')
