from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import ProductForm, ProductImagesFormSet
from .models import Product, Order
import re


def index(request):
    return render(request, 'index.html')


class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products_list'
    #ordering = '-created' # filtered by created datetime DESC
    paginate_by = 5  # Need to save order_type  state for right pagination

    def get_queryset(self):
        products = Product.objects.all()
        if self.request.GET.get('order_type') is None or self.request.GET.get('order_type')[0] == 'N':
            return products.order_by('-id')
        elif self.request.GET.get('order_type')[0] == 'B':
            return products.order_by('price')
        elif self.request.GET.get('order_type')[0] == 'Y':
            return products.order_by('-price')
        elif self.request.GET.get('order_type')[0] == 'C':
            return products.order_by('created')
        elif self.request.GET.get('order_type')[0] == 'H':
            return products.order_by('-created')

    def setup(self, request, *args, **kwargs) -> None:
        request.GET.get("page")
        request.META["QUERY_STRING"] = re.sub("(&|\?)page=(.)*", "", request.META.get("QUERY_STRING", ""))
        return super().setup(request, *args, **kwargs)


# def product_instance(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     context = {'product': product}
#     return render(request, 'product_instance.html', context)
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


# def product_delete(request, pk):
#     Product.objects.get(id=pk).delete()
#     return redirect('index')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products_list')


def order_create(request, pk):
    if request.method == 'POST':
        product_instance = get_object_or_404(Product, id=pk)
        try:
            order_instance = get_object_or_404(Order, customer=request.user, status='Вп')
            order_instance.products.add(product_instance)
        except:
            order_new = Order.objects.create(
            name=request.user.first_name,
            surname=request.user.last_name,
            patronymic=request.user.patronymic,
            email=request.user.email,
            phone=request.user.phone,
            region=request.user.region,
            city=request.user.city,
            street_name=request.user.street_name,
            house_number=request.user.house_number,
            entrance=request.user.entrance,
            floor=request.user.floor,
            apartment=request.user.apartment,
            post_code=request.user.post_code,
            customer=request.user,
            )
            order_new.products.add(product_instance)

    return redirect('profile')
