from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UsuarioSerializer, CidadeEstadoSerializer, serializers
from .models import Usuario, CidadeEstado

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        s_user = UserSerializer(data=request.data)
        if s_user.is_valid():
            
            try:
                data = s_user.save()
                return Response({
                    "user": {
                        "id": data["user"].id,
                        "username": data["user"].username,
                        "email": data["user"].email,
                    },
                    "token": data["token"]
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


@api_view(['GET', 'PUT'])
def visualizar_perfil(request):
    if not request.user.groups.filter(name="dono_centro_poliesportivo").exists():
        return Response({"Situação": "Permissão negada."})
    
    if request.method == 'GET':
        usuario = Usuario.objects.filter(user=request.user.id).first()

        if usuario:
            s_usuario = UsuarioSerializer(instance=usuario)
            residencia = CidadeEstado.objects.get(pk=s_usuario['residencia'].value)
            s_residencia = CidadeEstadoSerializer(instance=residencia)

            return Response({"usuario": s_usuario.data, "residencia": s_residencia.data})
        else:
            return Response({"Erro":"achei não"})