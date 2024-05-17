from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product


def index(request):
    return render(request, 'index.html')


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products_list'
    ordering = '-created'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_instance.html'
    context_object_name = 'product'


def product_delete(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('index')


# def product_instance(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     context = {'product': product}
#     return render(request, 'product_instance.html', context)

