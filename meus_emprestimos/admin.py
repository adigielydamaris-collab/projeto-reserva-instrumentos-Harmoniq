from django.contrib import admin
from .models import Emprestimos

@admin.register(Emprestimos)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ["status"]
   
