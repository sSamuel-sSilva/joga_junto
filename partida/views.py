from django.shortcuts import render
import json
from rest_framework import generics
from .models import AgendamentoPartida, UsuarioAgendamento, Usario
from centro_poliesportivo.models import Quadra, AuxPartida, CentroPoliesportivo, Modalidade
from .serializers import AgendamentoPartidaSerializers, UsarioAgendamentoSerializers, UsarioSerializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime


class AgendamentoPartidaListCreate(generics.ListCreateAPIView):
    queryset = AgendamentoPartida.objects.all()
    serializer_class = AgendamentoPartidaSerializers

class AgendamentoPartidaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgendamentoPartida.objects.all()
    serializer_class = AgendamentoPartidaSerializers



class UsarioAgendamentoListCreate(generics.ListCreateAPIView):
    queryset = UsuarioAgendamento.objects.all()
    serializer_class = UsarioAgendamentoSerializers

class UsarioAgendamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioAgendamento.objects.all()
    serializer_class = UsarioAgendamentoSerializers



class UsarioListCreate(generics.ListCreateAPIView):
    queryset = Usario.objects.all()
    serializer_class = UsarioSerializers

class UsarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usario.objects.all()
    serializer_class = UsarioSerializers


@csrf_exempt
def cadastrar_partida(request, id):
    if request.method == 'GET':
        return HttpResponse("GET")

    
    elif request.method == 'POST':
        data = json.loads(request.body)

        lider = Usario.objects.filter(pk=id)[0]
        
        ct_pol = data['centro_poliesportivo']
        modalidade = data['modalidade']
        data_part = data['data']
        horario_inicio = data['horario_inicio']
        horario_termino = data['horario_termino']
        convidados = data['convidados']

        res = disponibilidade(data_part, horario_inicio, horario_termino, ct_pol, modalidade)

        if (res == -2):
            return HttpResponse("Sem quadras para essa modalidade")
        elif (res == -1):
            return HttpResponse("Todas as quadras com essa modalidade estão ocupadas")
        
        aux_part = AuxPartida.objects.filter(ct_pol=ct_pol, modalidade=modalidade)[0]

        print(aux_part.quantidade_minima)
        if len(convidados) < aux_part.quantidade_minima:
            return HttpResponse("Jogadores Insuficientes")

        ct_pol = CentroPoliesportivo.objects.filter(id=ct_pol)[0]
        modalidade = Modalidade.objects.filter(id=modalidade)[0]

        agen_part = AgendamentoPartida (
            lider_partida=lider,
            centro_poliesportivo=ct_pol,
            modalidade=modalidade,
            data=data_part,
            horario_inicio=horario_inicio,
            horario_termino=horario_termino,
            valor_final = aux_part
        )

        try:
            agen_part.save()
        except Exception as e:
            print(f'ERRO AGENDAMENTO_PARTIDA: {e}')
        else:

            for convidado in convidados:
                c__ = Usario.objects.filter(id=convidado)[0]
                c = UsuarioAgendamento (
                    usuario = c__,
                    agendamento_partida = agen_part 
                )

                try:
                    c.save()
                except Exception as e:
                    print(f'ERRO USUARIO_AGENDAMENTO: {e}')
        
        return HttpResponse("JOIA")

def disponibilidade(data, horario_inicio, horario_fim, ct, modalidade):
    partidas = AgendamentoPartida.objects.filter(data=data, centro_poliesportivo=ct)

    quantidade_partidas_dia = 0
    quantidade_quadras = len(Quadra.objects.filter(modalidade=modalidade, ct_pol=ct))

    horario_inicio = datetime.strptime(horario_inicio, "%H:%M:%S").time()
    horario_fim = datetime.strptime(horario_fim, "%H:%M:%S").time()


    if partidas:
        for partida in partidas:
            if (horario_fim > partida.horario_inicio) or (horario_inicio < partida.horario_fim):
                quantidade_partidas_dia = quantidade_partidas_dia + 1

    if quantidade_quadras > quantidade_partidas_dia:
        return 1
    elif quantidade_quadras <= 0:
        return -2
    else: 
        return -1
