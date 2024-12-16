from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('newdata/', views.input_data, name='input_data'),
    path('view/', views.view_data, name='view_data'),

    path('accounts/login/', include('django.contrib.auth.urls')),

    path('accounts/', include('django.contrib.auth.urls')), # For authentication views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
]