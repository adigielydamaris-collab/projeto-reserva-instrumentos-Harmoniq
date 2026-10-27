from django.db import models
from instrumentos.models import Instrumentos

class Emprestimos (models.Model):
    data = models.DateField()
    hora = models.TimeField()
    instrumento = models.ForeignKey(Instrumentos,related_name="instrumentos", on_delete= models.CASCADE)
    status = models.CharField(max_length=100, choices=[("Confirmado","Confirmado"),("Pendente","Pendente"),
    ("Cacelado","Cacelado"),("Concluido","Concluido")])

    def __str__(self):
            return self.status

    

