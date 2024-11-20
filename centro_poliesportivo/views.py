from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import json
from django.http import Http404
from .models import Modalidade, PeriodoFuncionamento, CentroPoliesportivo, Quadra, AuxPartida, CidadeEstado
from .serializers import ModalidadeSerializer, PeriodoFuncionamentoSerializer, CentroPoliesportivoSerializer, QuadraSerializer, AuxPartidaSerializer
from usuario.serializers import UsuarioCentroPoliesportivoSerializer, CidadeEstadoSerializer
from django.views.decorators.csrf import csrf_exempt
from usuario.models import UsuarioCentroPoliesportivo


class ModalidadeListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer
         

class CidadeEstadoListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = CidadeEstado.objects.all()
    serializer_class = CidadeEstadoSerializer


class PeriodoFuncionamentoListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = PeriodoFuncionamento.objects.all()
    serializer_class = PeriodoFuncionamentoSerializer


class CentroPoliesportivoListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = CentroPoliesportivo.objects.all()
    serializer_class = CentroPoliesportivoSerializer


class QuadraListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = CentroPoliesportivo.objects.all()
    serializer_class = CentroPoliesportivoSerializer


class AuxPartidaListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = AuxPartida.objects.all()
    serializer_class = AuxPartidaSerializer



class ModalidadeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer



class CidadeEstadoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = CidadeEstado.objects.all()
    serializer_class = CidadeEstadoSerializer


class PeriodoFuncionamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = PeriodoFuncionamento.objects.all()
    serializer_class = PeriodoFuncionamentoSerializer



class CentroPoliesportivoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = CentroPoliesportivo.objects.all()
    serializer_class = CentroPoliesportivoSerializer



class QuadraRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer



class AuxPartidaSerializersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = AuxPartida.objects.all()
    serializer_class = AuxPartidaSerializer



@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def ctpol_list_create(request):
    if not request.user.groups.filter(name="dono_centro_poliesportivo").exists():
        return Response({"Situação": "Permissão negada."})

    if request.method == 'GET':
        user = request.user

        ctpols_user = UsuarioCentroPoliesportivo.objects.filter(user=user.id)
        
        if not ctpols_user:
            return Response({"Situação": "Usuario não possui Centros Poliesportivos cadastrados."})
        
        ctpols = []

        for c in ctpols_user:
            ct = CentroPoliesportivo.objects.get(pk=c.ctpol.pk)
            ctpols.append(ct)

        


        quant_ctpol = len(ctpols)
        json_ctpols = []

        for i in range(quant_ctpol):
            qs_quadras = Quadra.objects.filter(ct_pol=ctpols[i].pk)
            qs_periodos_func = PeriodoFuncionamento.objects.filter(ct_pol=ctpols[i].pk)
            qs_aux_partida = AuxPartida.objects.filter(ct_pol=ctpols[i].pk)
            
            quadras = [
                {
                    "pk": q.pk, 
                    "modalidade": q.modalidade.modalidade 
                }
                    for q in qs_quadras
            ]

            periodos_func = [
                {
                    "pk": pf.pk,
                    "dia_da_semana": pf.dia_da_semana,
                    "horario_abertura": pf.horario_abertura.strftime("%H:%M:%S"),
                    "horario_fechamento": pf.horario_fechamento.strftime("%H:%M:%S")
                }

                for pf in qs_periodos_func 
            ]

            aux_partida = [
                {
                    "pk": ap.pk,
                    "modalidade" : ap.modalidade.modalidade,
                    "quantidade_minima": ap.quantidade_minima,
                    "valor_final": ap.valor_final
                }
                for ap in qs_aux_partida
            ]

            r_modelo = CidadeEstado.objects.get(pk=ctpols[i].residencia.pk)

            residencia = {
                "pk": r_modelo.pk,
                "cidade": r_modelo.cidade,
                "estado": r_modelo.estado
            } 

            # print(residencia)
            ctpol_atual = {
                "ctpol": {
                    "pk": ctpols[i].pk,
                    "nome": ctpols[i].nome,
                    "residencia": residencia,
                    "numero": ctpols[i].numero,
                    "rua": ctpols[i].rua,
                    "quantidade_quadras": ctpols[i].quantidade_quadras,
                    "contato": ctpols[i].contato,
                    "descricao": ctpols[i].descricao,
                    "avaliacao": ctpols[i].avaliacao,
                },

                "quadras": quadras,
                "periodos_func": periodos_func,
                "aux_partida": aux_partida
            }

            json_ctpols.append(ctpol_atual)

        return Response(json_ctpols)

    elif request.method == 'POST':
        data = json.loads(request.body)
        
        ct_pol_json = data.get('ct_pol')
        residencia_json = data.get('residencia')
        quadras_json = data.get('quadras')
        aux_partida_json = data.get('aux_partida')
        periodos_func_json = data.get('periodos_func')

        ctpol_info = {
            "nome": ct_pol_json.get('nome'),
            "numero": ct_pol_json.get('numero'),
            "rua": ct_pol_json.get('rua'),
            "quantidade_quadras": len(quadras_json),
            "contato": ct_pol_json.get('contato'),
            "descricao": ct_pol_json.get('descricao'),
            "avaliacao": 0
        }


        cidade_estado = CidadeEstado.objects.get(cidade=residencia_json['cidade'], estado=residencia_json['estado'])
        ctpol_info['residencia'] = cidade_estado.pk
        

        # cadastrando o ct
        s_ct_pol = CentroPoliesportivoSerializer(data=ctpol_info)
        if not s_ct_pol.is_valid():
            print("ERRO CTPOL")
            return Response(s_ct_pol.errors, status=status.HTTP_400_BAD_REQUEST)
        ct_pol = s_ct_pol.save()

        id_ct_pol = ct_pol.id


        # cadastrando as quadras do ct
        print(len(quadras_json))
        for i in range(int(len(quadras_json['modalidade']))):
            quadra = {
                "ct_pol": id_ct_pol,
                "modalidade": quadras_json["modalidade"][i]
            }

            s_quadra = QuadraSerializer(data=quadra)
            if not s_quadra.is_valid():
                print(f"ERRO QUADRA: {i}")
                return Response(s_quadra.errors, status=status.HTTP_400_BAD_REQUEST)

            s_quadra.save()


        # # cadastrando os aux_parts
        quantidade_aux_parts = len(aux_partida_json)
        for i in range(quantidade_aux_parts):
            aux_part = {
                "ct_pol": id_ct_pol,
                "modalidade": aux_partida_json[i]['modalidade'],
                "quantidade_minima": aux_partida_json[i]['quantidade_minima'],
                "valor_final": aux_partida_json[i]['valor_final'],
            }

            s_aux_part = AuxPartidaSerializer(data = aux_part)
            if not s_aux_part.is_valid():
                print(f"ERRO AUX_PART: {i}")
                return Response(s_aux_part.errors, status=status.HTTP_400_BAD_REQUEST)

            s_aux_part.save()


        # cadastrando os periosdos de funcionamento
        quantidade_periodos_func = len(periodos_func_json['dias_da_semana'])
        for i in range(quantidade_periodos_func):
            periodo_func = {
                "ct_pol": id_ct_pol,
                "dia_da_semana": periodos_func_json['dias_da_semana'][i],
                "horario_abertura": periodos_func_json['horarios_abertura'][i],
                "horario_fechamento": periodos_func_json['horarios_fechamento'][i],
            }

            s_periodos_func = PeriodoFuncionamentoSerializer(data=periodo_func)
            if not s_periodos_func.is_valid():
                print(f"ERRO AUX_PART: {i}")
                return Response(s_periodos_func.errors, status=status.HTTP_400_BAD_REQUEST)

            s_periodos_func.save()

        s_user_ctpol = UsuarioCentroPoliesportivoSerializer(data=
                                                            {"user": request.user.id,
                                                             "ctpol": id_ct_pol})    
        if not s_user_ctpol.is_valid():
            print(f"ERRO RELAÇÂO USUARIO-CTPOL")
            return Response(s_periodos_func.errors, status=status.HTTP_400_BAD_REQUEST)

        s_user_ctpol.save()

        return Response({"status": "cadastrado com sucesso"}, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
@api_view(['GET', 'PUT', 'DELETE'])
def ctpol_detail(request, pk):

    if not request.user.groups.filter(name="dono_centro_poliesportivo").exists():
        return Response({"Situação": "Permissão negada."})

    if request.method == 'GET':
        ct_pol = get_object(pk, True)
        return Response(ct_pol)


    if request.method == 'PUT':
        ct_pol_request = request.data
        ct_pol = CentroPoliesportivo.objects.get(pk=pk)
        ct_pol_request['ct_pol']["avaliacao"] = ct_pol.avaliacao

        s_ct_pol = CentroPoliesportivoSerializer(ct_pol, data=ct_pol_request['ct_pol'])
        if not s_ct_pol.is_valid():
            return Response(s_ct_pol.errors, status=status.HTTP_400_BAD_REQUEST)
        s_ct_pol.save()

        print(ct_pol_request)

        for i in range(len(ct_pol_request['quadras'])):
            print(ct_pol_request['quadras'][i]['pk'])
            quadra = Quadra.objects.get(pk=ct_pol_request['quadras'][i]['pk'])
            ct_pol_request['quadras'][i]['ct_pol'] = pk
            s_quadra = QuadraSerializer(quadra, data=ct_pol_request['quadras'][i])
            if not s_quadra.is_valid():
                print(f"ERRO S_QUADRA {i} UPDATE")
                return Response(s_quadra.errors, status=status.HTTP_400_BAD_REQUEST)
            s_quadra.save()

        for i in range(len(ct_pol_request['periodos_func'])):
            periodo_func = PeriodoFuncionamento.objects.get(pk=ct_pol_request['periodos_func'][i]['pk'])
            ct_pol_request['periodos_func'][i]['ct_pol'] = pk
            s_periodo_func = PeriodoFuncionamentoSerializer(periodo_func, data=ct_pol_request['periodos_func'][i])
            if not s_periodo_func.is_valid():
                print(f"ERRO S_PERIODO_FUNC {i} UPDATE")
                return Response(s_periodo_func.errors, status=status.HTTP_400_BAD_REQUEST)
            s_periodo_func.save()

        for i in range(len(ct_pol_request['aux_partida'])):
            aux_partida = AuxPartida.objects.get(pk=ct_pol_request['aux_partida'][i]['pk'])
            ct_pol_request['aux_partida'][i]['ct_pol'] = pk
            s_aux_partida = AuxPartidaSerializer(aux_partida, data=ct_pol_request['aux_partida'][i])
            if not s_aux_partida.is_valid():
                print(f"ERRO S_AUX_PARTIDA {i} UPDATE")
                return Response(s_aux_partida.errors, status=status.HTTP_400_BAD_REQUEST)
            s_aux_partida.save()

        return Response(ct_pol_request)
        
    
    if request.method == 'DELETE':
        try:
            
            ct_pol = CentroPoliesportivo.objects.get(pk=pk)
            ct_pol.delete()

            ct_pol_user = UsuarioCentroPoliesportivo.objects.filter(ctpol=pk).first()
            ct_pol_user.delete()

            return Response({"Deleteção": "Concluída chefe."})
        except CentroPoliesportivo.DoesNotExist:
            raise Http404

def get_object(pk, get=False):
    obj_json = {}
    quadras = []

    if get:
        try:
            ct_pol = CentroPoliesportivo.objects.get(pk=pk)
        except CentroPoliesportivo.DoesNotExist:
            raise Http404
        
        
        r_modelo = CidadeEstado.objects.get(pk=ct_pol.residencia.pk)
        residencia = {
            "pk": r_modelo.pk,
            "cidade": r_modelo.cidade,
            "estado": r_modelo.estado
        } 

        obj_json["ct_pol"] = {
            "pk": ct_pol.pk,
            "nome": ct_pol.nome,
            "residencia": residencia,
            "numero": ct_pol.numero,
            "rua": ct_pol.rua,
            "quantidade_quadras": ct_pol.quantidade_quadras,
            "contato": ct_pol.contato,
            "descricao": ct_pol.descricao,
            "avaliacao": ct_pol.avaliacao,
        }

        obj_json["quadras"] = [
            {
                "pk": q.pk,
                "modalidade": q.modalidade.modalidade
            }
            for q in list(Quadra.objects.filter(ct_pol=pk))
        ]

        obj_json["periodos_func"] = [   
            {
                "pk": pf.pk,
                "dia_da_semana": pf.dia_da_semana,
                "horario_abertura": pf.horario_abertura.strftime("%H:%M:%S"),
                "horario_fechamento": pf.horario_fechamento.strftime("%H:%M:%S")
            } for pf in list(PeriodoFuncionamento.objects.filter(ct_pol=pk) )
        ]

        obj_json["aux_partida"] = [
                {
                    "pk": ap.pk,
                    "modalidade" : ap.modalidade.modalidade,
                    "quantidade_minima": ap.quantidade_minima,
                    "valor_final": ap.valor_final
                }
                for ap in list(AuxPartida.objects.filter(ct_pol=pk))
            ]
        
        return obj_json
    

    try:
        ct_pol = CentroPoliesportivo.objects.get(pk=pk)
    except CentroPoliesportivo.DoesNotExist:
        raise Http404
    
    obj_json["ct_pol"] = ct_pol

    obj_json["quadras"] = list(Quadra.objects.filter(ct_pol=pk))

    obj_json["periodos_func"] = list(PeriodoFuncionamento.objects.filter(ct_pol=pk))

    obj_json["aux_partida"] = list(AuxPartida.objects.filter(ct_pol=pk))
    
    return obj_json
        
