from rest_framework import status
from rest_framework import generics
from .models import AgendamentoPartida, UsuarioAgendamento
from centro_poliesportivo.models import Quadra, AuxPartida, CentroPoliesportivo, Modalidade, PeriodoFuncionamento
from .serializers import AgendamentoPartidaSerializers, UsuarioAgendamentoSerializers
from datetime import datetime
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usuario.models import Usuario, User, CidadeEstado


class AgendamentoPartidaListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = AgendamentoPartida.objects.all()
    serializer_class = AgendamentoPartidaSerializers


class AgendamentoPartidaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = AgendamentoPartida.objects.all()
    serializer_class = AgendamentoPartidaSerializers


class UsuarioAgendamentoListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = UsuarioAgendamento.objects.all()
    serializer_class = UsuarioAgendamentoSerializers


class UsuarioAgendamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = UsuarioAgendamento.objects.all()
    serializer_class = UsuarioAgendamentoSerializers


def dia_semana(data):
    data_obj = datetime.strptime(data, "%Y-%m-%d")
    dia_semana = data_obj.weekday()
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    return dias_semana[dia_semana]


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def cadastrar_listar_partida(request):
    if not request.user.groups.filter(name="jogador").exists():
        return Response({"Situação": "Permissão negada."})
    
    if request.method == 'GET':
        dados = []

        residencia_user = Usuario.objects.filter(user=request.user.id).first().residencia.id
        
        ctpol = request.GET.get('ctpol')
        modalidade = request.GET.get('modalidade')

        print(ctpol, modalidade, residencia_user)


        partidas = AgendamentoPartida.objects.filter(residencia=residencia_user)
        if not partidas:
            return Response({"Situação": "Sem partidas encontradas na sua região."});


        if ctpol and modalidade:
            partidas = AgendamentoPartida.objects.filter(centro_poliesportivo=ctpol, modalidade=modalidade)

        elif modalidade:
            partidas = AgendamentoPartida.objects.filter(modalidade=modalidade)

        elif ctpol:
            partidas = AgendamentoPartida.objects.filter(centro_poliesportivo=ctpol)
        
        if not partidas:
            return Response({"Situação": "Sem partidas encontradas para essa filtragem."})


        nesse_momento = datetime.now()
        dia_desse_momento = nesse_momento.date()
        hora_desse_momento = nesse_momento.time()

        partidas = AgendamentoPartida.objects.filter(data__gt=dia_desse_momento, horario_inicio__gt=hora_desse_momento)

        if not partidas:
            return Response({"Situação": "Sem partidas encontradas nesse momento."})
        

        for p in partidas:
            dia_semana_partida = dia_semana(str(p.data))

            lider_info = Usuario.objects.filter(user=p.lider_partida.id).first()
            dados.append({
                "lider": lider_info.nome_completo,
                "data": f"{p.data}, {dia_semana_partida}",
                "inicio": p.horario_inicio,
                "fim": p.horario_termino,
                "modalidade": p.modalidade.__str__(),
                "residencia": p.residencia.__str__(),
                "ct": p.centro_poliesportivo.__str__()
            })

        return Response(dados)


    if request.method == 'POST':
        data = request.data
        id_user = request.user.id
        id_ctpol = data.get('ct_pol')
        horario_inicio_original = data.get('horario_inicio')
        horario_fim_original = data.get('horario_fim')
        data_partida = data.get('data')
        modalidade = data.get('modalidade')
        jogadores = data.get('jogadores')

        horario_inicio = datetime.strptime(horario_inicio_original, "%H:%M:%S").time()
        horario_fim = datetime.strptime(horario_fim_original, "%H:%M:%S").time()

        dia_semana_partida = dia_semana(data_partida)

        dia_funcionamento = PeriodoFuncionamento.objects.filter(ct_pol=id_ctpol, dia_da_semana=dia_semana_partida).first()

        if not dia_funcionamento:
            return Response({"Situação": "CT não abre esse dia."})

        if horario_inicio < dia_funcionamento.horario_abertura or horario_fim > dia_funcionamento.horario_fechamento:
            return Response({"Situação": "Horarios inválidos."})
        
        quadras = Quadra.objects.filter(ct_pol=id_ctpol, modalidade=modalidade)
        if not quadras:
            return Response({"Situação": "O CT não possui quadras para esta modalidade."})

        
        aux_partida = AuxPartida.objects.filter(ct_pol=id_ctpol, modalidade=modalidade).first()
        if aux_partida.quantidade_minima > len(jogadores) + 1:
            return Response({"Situação": "Quantidade de jogadores insuficiente."})

        
        partidas_do_dia = AgendamentoPartida.objects.filter(centro_poliesportivo=id_ctpol, modalidade=modalidade, data=data_partida)
        if partidas_do_dia:
            for partida in partidas_do_dia:
                if (partida.horario_inicio <= horario_inicio <= partida.horario_termino) or (partida.horario_inicio <= horario_fim <= partida.horario_termino) or (horario_inicio < partida.horario_inicio and horario_fim > partida.horario_termino):
                    return Response({"Situação": "Conflito de horarios entre partidas."})
                
        
        valor_final = aux_partida.valor_final
        residencia = CentroPoliesportivo.objects.get(pk=id_ctpol).residencia.pk

        partida_atual = {
            "lider_partida": id_user,
            "centro_poliesportivo": id_ctpol,
            "modalidade": modalidade,
            "residencia": residencia,
            "data": data_partida,
            "horario_inicio": horario_inicio_original,
            "horario_termino": horario_fim_original,
            "valor_final": valor_final,
        }

        s_partida_atual = AgendamentoPartidaSerializers(data=partida_atual)
        if not s_partida_atual.is_valid():
            return Response({"Erro no cadastro da partida": s_partida_atual.errors}, status=status.HTTP_400_BAD_REQUEST)
        p = s_partida_atual.save()

        partida_id = p.id

        for s in jogadores:
            s_usuario_partida = UsuarioAgendamentoSerializers(data={"usuario": s, "agendamento_partida": partida_id})
            if not s_usuario_partida.is_valid():
                return Response({"Erro no cadastro dos jogadores na partida": s_usuario_partida.errors}, status=status.HTTP_400_BAD_REQUEST)
            s_usuario_partida.save()


        return Response({"Cadastro feito": s_partida_atual.data})


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def partida_detalhe(request, id):
    if not request.user.groups.filter(name="jogador").exists():
        return Response({"Situação": "Permissão negada."})
    
    if request.method == 'GET':
        partida = AgendamentoPartida.objects.get(pk=id)
        jogadores = UsuarioAgendamento.objects.filter(agendamento_partida=id)
        lider_info = Usuario.objects.filter(user=partida.lider_partida.id).first()

        jogadores_info = []

        for j in jogadores:
            jog = Usuario.objects.filter(user=j.id).first()
            jogadores_info.append(jog.__str__())

        p = {
            "lider": lider_info.__str__(),
            "data": partida.data,
            "inicio": partida.horario_inicio,
            "fim": partida.horario_termino,
            "modalidade": partida.modalidade.__str__(),
            "residencia": partida.residencia.__str__(),
            "ct": partida.centro_poliesportivo.__str__(),
            "valor": partida.valor_final,
            "jogadores": jogadores_info
        }

        return Response(p)