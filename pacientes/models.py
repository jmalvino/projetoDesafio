from django.db import models
from datetime import datetime

# Create your models here.

class Pacientes(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)  
    pais = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    dataDeCriacao = models.DateTimeField(auto_now_add=True)

    #metodo que mostra no banco de dados o nome definido
    def __str__(self):
        return self.nome




