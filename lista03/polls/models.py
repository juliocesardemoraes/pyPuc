import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome