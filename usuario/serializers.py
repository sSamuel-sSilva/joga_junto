from django.db import IntegrityError
from .models import Usuario, UsuarioEsportes, User
from rest_framework import serializers
    

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['user']


class UsuarioEsportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEsportes
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'usuario']

    def create(self, validated_data):
        usuario = validated_data.pop('usuario')

        # try:
        user = User.objects.create(
                username=validated_data.get('username'),
                email=usuario.get('email')
            )
        
        user.set_password(validated_data.get('password'))
        user.save()

        Usuario.objects.create(user=user, **usuario)
        return user
        
        # except IntegrityError as erro:
        #     raise serializers.ValidationError(f"Erro registro usario: {erro}")


    def update(self, instance, validated_data):
        usuario = validated_data.pop('usuario', {})
        usuario_instancia = instance.usuario

        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        usuario_instancia.nome_completo = usuario.get('nome_completo', instance.nome_completo)
        usuario_instancia.residencia = usuario.get('residencia', instance.residencia)
        usuario_instancia.data_nascimento = usuario.get('data_nascimento', instance.data_nascimento)
        usuario_instancia.partidas_concluidas = usuario.get('partidas_concluidas', instance.partidas_concluidas)
        usuario_instancia.contato = usuario.get('contato', instance.contato)

        return instance