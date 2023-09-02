from django.urls import path
from . import views

urlpatterns = [
    path('app/sumar/<int:num1>/<int:num2>/', views.sumar, name='sumar'),
    path('app/restar/<int:num1>/<int:num2>/', views.restar, name='restar'),
    path('app/multiplicar/<int:num1>/<int:num2>/', views.multiplicar, name='multiplicar'),
]

