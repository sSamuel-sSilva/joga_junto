from django.db import models


class Modalidade(models.Model):
    modalidade = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.modalidade


class CidadeEstado(models.Model):
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.cidade}/{self.estado}"

class CentroPoliesportivo(models.Model):
    nome = models.CharField(max_length=60)
    residencia = models.ForeignKey(CidadeEstado, on_delete=models.DO_NOTHING)
    numero = models.IntegerField()
    rua = models.CharField(max_length=70)
    quantidade_quadras = models.IntegerField()
    contato = models.CharField(max_length=11)
    descricao = models.CharField(max_length=299)
    avaliacao = models.FloatField()

    def __str__(self) -> str:
        return self.nome


class AuxPartida(models.Model):
    ct_pol = models.ForeignKey(CentroPoliesportivo, null=False, on_delete=models.CASCADE)
    modalidade = models.ForeignKey(Modalidade, null=False, on_delete=models.DO_NOTHING)
    quantidade_minima = models.IntegerField()
    valor_final = models.FloatField()


class Quadra(models.Model):
    ct_pol = models.ForeignKey(CentroPoliesportivo, on_delete=models.CASCADE, null=False)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.DO_NOTHING, null=False)


class PeriodoFuncionamento(models.Model):
    ct_pol = models.ForeignKey(CentroPoliesportivo, null=False, on_delete=models.CASCADE)
    dia_da_semana = models.CharField(max_length=10)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()
