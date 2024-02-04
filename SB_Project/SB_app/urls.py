from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView),
    path('login', views.LoginView),
    path('form', views.FormView),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]