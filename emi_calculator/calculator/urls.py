from django.urls import path
from . import views

urlpatterns = [
    path('', views.emi_calculator_view, name='emi_calculator'),
    path('calculate_emi/', views.calculate_emi, name='calculate_emi'),
]
