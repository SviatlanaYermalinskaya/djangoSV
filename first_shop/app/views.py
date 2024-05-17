from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product


# Create your views here.
def hello(request):
    return HttpResponse("Hello")


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def product_delete(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('index')


def product_instance(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}
    return render(request, 'product_instance.html', context)

