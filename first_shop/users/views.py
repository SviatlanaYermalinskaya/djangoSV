import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from app.models import Order
from .forms import RegistrationUserForm


class ProfileView(ListView, LoginRequiredMixin):
    template_name = 'profile.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created')


class RegistrationView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'register.html'

    def form_valid(self, form):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'q', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        random_code = [random.choice(alphabet) for letter in range(15)]

        instance = form.save(commit=False)
        email = self.request.POST.get('email')
        instance.username = email.lower().partition('@')[0]
        instance.referral_code = ''.join(random_code)
        instance.save()

        return redirect('login')


class CustomLoginView(LoginView):
    template_name = 'login.html'


# class CustomLogoutView(LogoutView):
#     #template_name = 'logout.html'   # is not required now so we can use LogoutView from django.contrib.auth.views
#     pass
