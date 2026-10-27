from django.db import models

class Instrumentos (models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=[("Cordas","Cordas"),("Sopro","Sopro"),
    ("Percussão","Percussão"),("Teclas","Teclas")])
    descrição = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

