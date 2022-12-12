from django.test import TestCase

from apps.pacientes.models import Paciente


class PacienteTest(TestCase):
    def setUpTest(self):
        super(PacienteTest, self).setUp()
        self.paciente = Paciente.objects.create(nome="Joao", idade=1, endereco="Rua da conceiçao, 199")

    def unicode(self):
        self.assertEqual()
