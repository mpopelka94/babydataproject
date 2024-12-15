from django.urls import path
from . import views

urlpatterns = [
    path('newdata/', views.input_data, name='input_data'),
    path('view/', views.view_data, name='view_data'),

    path('', views.home, name='home'),
]