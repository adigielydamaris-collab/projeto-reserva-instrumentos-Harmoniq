from django.urls import path

from . import views

app_name = 'meus_emprestimos'

urlpatterns = [
    path('', views.meus_emprestimosView, name='meus_emprestimos'),
]