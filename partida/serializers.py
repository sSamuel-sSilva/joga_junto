from rest_framework import serializers
from .models import UsuarioAgendamento, Usario, AgendamentoPartida

class UsarioAgendamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAgendamento
        fields = '__all__'


class UsarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usario
        fields = '__all__'


class AgendamentoPartidaSerializers(serializers.ModelSerializer):
    class Meta:
        model = AgendamentoPartida
        fields = '__all__'
