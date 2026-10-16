from django.shortcuts import render

# Create your views here.
def instrumentosView(request):
    return render(request, "instrumentos/lista.html")