from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def categoria(request):
    return render(request, 'categoria.html')