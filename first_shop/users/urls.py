from django.urls import path
from django.contrib.auth.views import LogoutView

from users import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
