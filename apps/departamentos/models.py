from django.db import models

# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=100)