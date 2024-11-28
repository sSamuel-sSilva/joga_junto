from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UsuarioSerializer, CidadeEstadoSerializer, UsuarioEsportesSerializer, serializers
from .models import Usuario, CidadeEstado, UsuarioEsportes

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        modalidades = data.pop('modalidades', None)

        s_user = UserSerializer(data=request.data)
        if s_user.is_valid():
            try:
                user = s_user.save()
                usuario = user.usuario

                if modalidades:
                    for m in modalidades:
                        modal = UsuarioEsportesSerializer(data={"usuario": user.usuario.id, "esporte": m})
                        if not modal.is_valid():
                            return Response(modal.errors, status=status.HTTP_400_BAD_REQUEST)
                        
                        modal.save()
                
                token, _=Token.objects.get_or_create(user=user)

                return Response({
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                    "token": token.key
                }, status=status.HTTP_201_CREATED)
             
            except serializers.ValidationError as erro:
                return Response({"Erro no cadastro": erro}, status=status.HTTP_400_BAD_REQUEST)


        else:
            return Response({"Erro": s_user.errors}, status=status.HTTP_400_BAD_REQUEST)


class loginView(APIView):
    permission_classes=[permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            token, _=Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data})
        else:
            return Response({"erro": "credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def visualizar_perfil(request):
    if not request.user.groups.filter(name="jogador").exists():
        return Response({"Situação": "Permissão negada."})
    
    if request.method == 'GET':
        usuario = Usuario.objects.filter(user=request.user.id).first()

        if usuario:
            
            usuario__ = {
                "nome_completo": usuario.nome_completo,
                "email": usuario.email,
                "data_nascimento": usuario.data_nascimento,
                "partidas_concluidas": usuario.partidas_concluidas,
                "contato": usuario.contato,
                "residencia": usuario.residencia.__str__(),
            }
            
            modalidades = []
            
            modals = UsuarioEsportes.objects.filter(usuario=usuario.id)

            for m in modals:
                modalidades.append(m.esporte.modalidade)


            return Response({"usuario": usuario__, "modalidades": modalidades})
        else:
            return Response({"Erro":"achei não"})