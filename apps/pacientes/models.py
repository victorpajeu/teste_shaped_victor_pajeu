from django.db import models


class Paciente(models.Model):
    nome = models.CharField("Nome", max_length=30)
    idade = models.IntegerField("Idade")
    endereco = models.CharField("Endereço", max_length=100)


