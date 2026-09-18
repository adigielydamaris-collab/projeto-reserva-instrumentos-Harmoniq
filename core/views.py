from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, "core/login.html")

def listagem(request):
    return render(request, "core/listagem.html")