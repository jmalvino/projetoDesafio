from django.db import models
from datetime import datetime

# Create your models here.

class Medicos(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    dataDeCriacao = models.DateTimeField()


#metodo que mostra no banco de dados o nome definido
def __str__(self):
    return self.email
