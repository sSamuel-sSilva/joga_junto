from rest_framework import generics
from django.http import HttpResponse
import json
from .models import Modalidade, PeriodoFuncionamento, CentroPoliesportivo, Quadra, AuxPartida
from .serializers import ModalidadeSerializers, PeriodoFuncionamentoSerializers, CentroPoliesportivoSerializers, QuadraSerializers, AuxPartidaSerializers
from django.views.decorators.csrf import csrf_exempt

class ModalidadeListCreate(generics.ListCreateAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializers


class ModalidadeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializers


class PeriodoFuncionamentoListCreate(generics.ListCreateAPIView):
    queryset = PeriodoFuncionamento.objects.all()
    serializer_class = PeriodoFuncionamentoSerializers


class PeriodoFuncionamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PeriodoFuncionamento.objects.all()
    serializer_class = PeriodoFuncionamentoSerializers


class CentroPoliesportivoListCreate(generics.ListCreateAPIView):
    queryset = CentroPoliesportivo.objects.all()
    serializer_class = CentroPoliesportivoSerializers


class CentroPoliesportivoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CentroPoliesportivo.objects.all()
    serializer_class = CentroPoliesportivoSerializers


class QuadraListCreate(generics.ListCreateAPIView):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializers


class QuadraRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializers


class AuxPartidaListCreate(generics.ListCreateAPIView):
    queryset = AuxPartida.objects.all()
    serializer_class = AuxPartidaSerializers


class AuxPartidaSerializersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuxPartida.objects.all()
    serializer_class = AuxPartidaSerializers


@csrf_exempt
def cadastrar_ct_pol(request):
    
    if request.method == 'GET':
        return HttpResponse("GET")

    elif request.method == 'POST':
        data = json.loads(request.body)
    
        nome = data['nome']
        cep = data['cep']
        numero = data['numero']
        quantidade_quadras = data['quantidade_quadras']
        contato_dono = data['contato_dono']
        descricao = data['descricao']

        modalidades = data['modalidade']
        quantidades_minimas = data['quantidade_minima']
        valores_finais = data['valor_final']

        dias_semana = data['dias_semana']
        horarios_abertura = data['horarios_abertura']
        horarios_fechamento = data['horarios_fechamento']



        ct = CentroPoliesportivo (
            nome = nome,
            cep = cep,
            numero = numero,
            quantidade_quadras = quantidade_quadras,
            contato_dono = contato_dono,
            descricao = descricao,
            avaliacao = 0
        )

        try:
            ct.save()
        except Exception as e:
            print(f"ERRO CT: {e}")


        ct_pol = CentroPoliesportivo.objects.filter(cep=cep, numero=numero)[0]


        for i, id_modalidade in enumerate(modalidades):
            m = Modalidade.objects.filter(id=id_modalidade)[0]

            quadra = Quadra (
                ct_pol = ct,
                modalidade = m
            )

            try:
                quadra.save()
            except Exception as e:
                print(f"ERRO QUADRA: {e}")

             
            aux_part = AuxPartida (
                ct_pol = ct,
                modalidade = m,
                quantidade_minima = quantidades_minimas[i],
                valor_final = valores_finais[i]
            )

            try:
                aux_part.save()
            except Exception as e:
                print(f"ERRO AUX_PART: {e}")
        
        
        for i in range(len(dias_semana)):
            pf = PeriodoFuncionamento (
                ct_pol = ct,
                dia_da_semana = dias_semana[i],
                horario_abertura = horarios_abertura[i],
                horario_fechamento = horarios_fechamento[i]
            )

            try:
                pf.save()
            except Exception as e:
                print(f"ERRO PERIODO_FUNCIONAMENTO: {e}")


        return HttpResponse("JOIA")
    