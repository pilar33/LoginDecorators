from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def Inicio(request):
    return render(request,'index.html')

@login_required
def Productos(request):
    return render(request,'productos.html')