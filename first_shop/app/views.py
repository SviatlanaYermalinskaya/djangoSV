from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import ProductForm, ProductImagesFormSet
from .models import Product



def index(request):
    return render(request, 'index.html')


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products_list'
    ordering = '-created'
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_instance.html'
    context_object_name = 'product'


# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'product_create.html'
#     form_class = ProductForm
#     success_url = reverse_lazy('products_list')




def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save()
            formset = ProductImagesFormSet(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                return redirect('products_list')
    form = ProductForm()
    formset = ProductImagesFormSet()
    context = {'form': form, 'formset': formset}
    return  render(request, 'product_create.html', context)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products_list')


# def product_delete(request, pk):
#     Product.objects.get(id=pk).delete()
#     return redirect('index')


# def product_instance(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     context = {'product': product}
#     return render(request, 'product_instance.html', context)

