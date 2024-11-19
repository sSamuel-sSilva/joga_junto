from django.contrib.auth.models import AbstractUser
from django.db import models
from centro_poliesportivo.models import CidadeEstado, Modalidade

class Usuario(AbstractUser):
    residencia = models.ForeignKey(CidadeEstado, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    partidas_concluidas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


class UsuarioEsportes(models.Model):
    auth_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    esporte = models.ForeignKey(Modalidade, on_delete=models.DO_NOTHING)
