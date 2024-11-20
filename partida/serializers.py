from rest_framework import serializers
from .models import UsuarioAgendamento, AgendamentoPartida

class UsuarioAgendamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAgendamento
        fields = '__all__'


class AgendamentoPartidaSerializers(serializers.ModelSerializer):
    class Meta:
        model = AgendamentoPartida
        fields = '__all__'
