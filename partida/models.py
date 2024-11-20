from django.db import models
from usuario.models import Usuario
from centro_poliesportivo.models import CentroPoliesportivo, AuxPartida, Modalidade

class AgendamentoPartida(models.Model):
    lider_partida = models.CharField(max_length=20)
    centro_poliesportivo = models.ForeignKey(CentroPoliesportivo, null=False, on_delete=models.DO_NOTHING)
    modalidade = models.ForeignKey(Modalidade, null=False, on_delete=models.DO_NOTHING)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_termino = models.TimeField()
    valor_final = models.ForeignKey(AuxPartida, null=False, on_delete=models.DO_NOTHING)

    
class UsuarioAgendamento(models.Model):
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.DO_NOTHING)
    agendamento_partida = models.ForeignKey(AgendamentoPartida, null=False, on_delete=models.DO_NOTHING)
