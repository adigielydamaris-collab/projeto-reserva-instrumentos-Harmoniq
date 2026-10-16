from django.urls import path

from . import views

app_name = 'instrumentos'

urlpatterns = [
    path('', views.instrumentosView, name='instrumentos'),
]