from django.shortcuts import render


def meus_emprestimosView(request):
    return render(request, "meus_emprestimos/meus_emprestimos.html")