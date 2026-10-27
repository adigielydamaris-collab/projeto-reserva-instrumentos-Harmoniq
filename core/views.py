from django.shortcuts import render
from instrumentos.models import Instrumentos

def homeView(request):
    instrumentos = Instrumentos.objects.all()
    context = {
        "instrumentos":instrumentos
    }
    return render(request, "core/home.html",context)

def login(request):
    return render(request, "core/login.html")