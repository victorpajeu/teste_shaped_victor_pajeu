from django.db import models

# models
from apps.pacientes.models import Paciente


class Exame(models.Model):
    nome_profissional = models.CharField("Nome do Profissional", max_length=30)
    data_exame = models.DateTimeField("Data do Exame")
    peso = models.DecimalField("Peso", max_digits=7, decimal_places=2)
    altura = models.DecimalField("Peso", max_digits=4, decimal_places=2)
    paciente = models.ForeignKey(Paciente, verbose_name="Paciente", on_delete=models.CASCADE)


