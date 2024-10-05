from rest_framework import serializers
from .models import Modalidade, PeriodoFuncionamento, CentroPoliesportivo, Quadra, AuxPartida

class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        fields = '__all__'


class PeriodoFuncionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoFuncionamento
        fields = '__all__'


class CentroPoliesportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroPoliesportivo
        fields = '__all__'


class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'


class AuxPartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxPartida
        fields = '__all__'
