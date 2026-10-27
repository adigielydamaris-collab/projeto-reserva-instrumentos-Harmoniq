from django.contrib import admin
from .models import Instrumentos

@admin.register(Instrumentos)
class InstrumentosAdmin(admin.ModelAdmin):
    list_display = ["nome", "tipo", "descrição", "disponivel"]
    

