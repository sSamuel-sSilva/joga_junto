from django.contrib.auth.models import User
from django.db import models
from centro_poliesportivo.models import CidadeEstado, Modalidade

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    residencia = models.ForeignKey(CidadeEstado, on_delete=models.DO_NOTHING)
    data_nascimento = models.DateField()
    partidas_concluidas = models.IntegerField()
    contato = models.CharField(max_length=11)

    def __str__(self):
        return self.nome_completo


class UsuarioEsportes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    esporte = models.ForeignKey(Modalidade, on_delete=models.DO_NOTHING)
