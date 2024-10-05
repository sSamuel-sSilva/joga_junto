from django.db import models


class Modalidade(models.Model):
    modalidade = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.modalidade


class CentroPoliesportivo(models.Model):
    nome = models.CharField(max_length=60)
    cep = models.CharField(max_length=11, unique=True) #tirar
    numero = models.IntegerField()
    quantidade_quadras = models.IntegerField()
    contato_dono = models.CharField(max_length=11)
    descricao = models.CharField(max_length=299)
    avaliacao = models.FloatField()

    def __str__(self) -> str:
        return self.nome


class AuxPartida(models.Model):
    ct_pol = models.ForeignKey(CentroPoliesportivo, null=False, on_delete=models.DO_NOTHING)
    modalidade = models.ForeignKey(Modalidade, null=False, on_delete=models.DO_NOTHING)
    quantidade_minima = models.IntegerField()
    valor_final = models.FloatField()


class Quadra(models.Model):
    ct_pol = models.ForeignKey(CentroPoliesportivo, on_delete=models.DO_NOTHING, null=False)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.DO_NOTHING, null=False)


class PeriodoFuncionamento(models.Model):
    ct_pol = models.ForeignKey(CentroPoliesportivo, null=False, on_delete=models.CASCADE)
    dia_da_semana = models.CharField(max_length=10)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()