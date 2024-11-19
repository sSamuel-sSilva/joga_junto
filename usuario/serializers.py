from .models import Usuario, UsuarioEsportes 
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'residencia', 'data_nascimento', 'partidas_concluidas']


class UsuarioEsportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEsportes
        fields = '__all__'