from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('productos/', views.Productos, name='Productos'),
]
