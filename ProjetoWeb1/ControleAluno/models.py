from django.db import models

# Create your models here.

class Aluno(models.Model):
    nomeCompleto = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)