from rest_framework import serializers
from .models import Modalidade, PeriodoFuncionamento, CentroPoliesportivo, Quadra, AuxPartida

class ModalidadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        fields = '__all__'


class PeriodoFuncionamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeriodoFuncionamento
        fields = '__all__'


class CentroPoliesportivoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CentroPoliesportivo
        fields = '__all__'


class QuadraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'


class AuxPartidaSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuxPartida
        fields = '__all__'
