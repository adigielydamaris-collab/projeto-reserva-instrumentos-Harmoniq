from django.shortcuts import render
from .models import Instrumentos

def instrumentosView(request):
    instrumentos = Instrumentos.objects.all()
    context = {
        "instrumentos":instrumentos
    }
    return render(request, "instrumentos/lista.html",context)
def homeView(request):
    instrumentos = Instrumentos.objects.all()
    context = {
        "instrumentos":instrumentos
    }
    return render(request, "instrumentos/home.html",context)