from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .serializers import UserSerializer, UsuarioSerializer, serializers

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        s_user = UserSerializer(data=request.data)
        # s_usuario = UsuarioSerializer(data=request.data.get('usuario', {}))

        # if s_user.is_valid() and s_usuario.is_valid():
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
