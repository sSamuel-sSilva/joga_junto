from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.http import Http404, HttpResponse
from .models import Modalidade, PeriodoFuncionamento, CentroPoliesportivo, Quadra, AuxPartida
from .serializers import ModalidadeSerializer, PeriodoFuncionamentoSerializer, CentroPoliesportivoSerializer, QuadraSerializer, AuxPartidaSerializer
from django.views.decorators.csrf import csrf_exempt


class ModalidadeListCreate(APIView):
    def get(self, request, format=None):
        modals = Modalidade.objects.all()
        s_modals = ModalidadeSerializer(modals, many=True)
        return Response(s_modals.data)

    def post(self, request, format=None):
        modal_post = ModalidadeSerializer(request.data)
        if modal_post.is_valid():
            modal_post.save()
            return Response(modal_post.data, status=status.HTTP_201_CREATED)
        
        return Response(modal_post.error, status=status.HTTP_400_BAD_REQUEST)
         

class PeriodoFuncionamentoListCreate(APIView):
    def get(self, request, format=None):
        per_funcs = PeriodoFuncionamento.objects.all()
        s_per_funcs = PeriodoFuncionamentoSerializer(per_funcs, many=True)
        return Response(s_per_funcs.data)
    
    def post(self, request, format=None):
        per_func_post = PeriodoFuncionamentoSerializer(request.data)
        if per_func_post.is_valid():
            per_func_post.save()
            return Response(per_func_post.data, status=status.HTTP_201_CREATED)
        
        return Response(per_func_post.error, status=status.HTTP_400_BAD_REQUEST)


class CentroPoliesportivoListCreate(APIView):
    def get(self, request, format=None):
        ctpols = CentroPoliesportivo.objects.all()
        s_ctpols = CentroPoliesportivoSerializer(ctpols, many=True)
        return Response(s_ctpols.data)
    
    def post(self, request, format=None):
        ctpol_post = CentroPoliesportivoSerializer(request.data)
        if ctpol_post.is_valid():
            ctpol_post.save()
            return Response(ctpol_post.data, status=status.HTTP_201_CREATED)
        
        return Response(ctpol_post.error, status=status.HTTP_400_BAD_REQUEST)


class QuadraListCreate(APIView):
    def get(self, request, format=None):
        quadras = Quadra.objects.all()
        s_quadras = QuadraSerializer(quadras, many=True)
        return Response(s_quadras.data)
    
    def post(self, request, format=None):
        quadra_post = QuadraSerializer(request.data)
        if quadra_post.is_valid():
            quadra_post.save()
            return Response(quadra_post.data, status=status.HTTP_201_CREATED)
        
        return Response(quadra_post.error, status=status.HTTP_400_BAD_REQUEST)


class AuxPartidaListCreate(APIView):
    def get(self, request, format=None):
        aux_parts = AuxPartida.objects.all()
        s_aux_parts = AuxPartidaSerializer(aux_parts, many=True)
        return Response(s_aux_parts.data)
    
    def post(self, request, format=None):
        aux_part_post = AuxPartidaSerializer(request.data)
        if aux_part_post.is_valid():
            aux_part_post.save()
            return Response(aux_part_post.data, status=status.HTTP_201_CREATED)
        
        return Response(aux_part_post.error, status=status.HTTP_400_BAD_REQUEST)


class ModalidadeRetrieveUpdateDestroy(APIView):
    def get_object(self, pk):
        try:
            modal = Modalidade.objects.get(pk=pk)
        except Modalidade.DoesNotExist:
            raise Http404
        

    def get(self, request, pk, format=None):
        modal = self.get_object(pk)
        s_modal = ModalidadeSerializer(modal)
        return Response(s_modal.data)


    def update(self, request, pk, format=None):
        modal = self.get_object(pk)
        s_modal = ModalidadeSerializer(modal, data=request.data)
        if s_modal.is_valid():
            s_modal.save()
            return Response(s_modal.data)
        return Response(s_modal.error, status=status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, format=None):
        modal = self.get_object(pk)
        modal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeriodoFuncionamentoRetrieveUpdateDestroy(APIView):
    def get_object(self, pk):
        try:
            per_func = PeriodoFuncionamento.objects.get(pk=pk)
        except PeriodoFuncionamento.DoesNotExist:
            raise Http404
        

    def get(self, request, pk, format=None):
        per_func = self.get_object(pk)
        s_per_func = PeriodoFuncionamentoSerializer(per_func)
        return Response(s_per_func.data)


    def update(self, request, pk, format=None):
        per_func = self.get_object(pk)
        s_per_func = PeriodoFuncionamentoSerializer(per_func, data=request.data)
        if s_per_func.is_valid():
            s_per_func.save()
            return Response(s_per_func.data)
        return Response(s_per_func.error, status=status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, format=None):
        per_func = self.get_object(pk)
        per_func.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CentroPoliesportivoRetrieveUpdateDestroy(APIView):
    def get_object(self, pk):
        try:
            ct_pol = CentroPoliesportivo.objects.get(pk=pk)
        except CentroPoliesportivo.DoesNotExist:
            raise Http404
        

    def get(self, request, pk, format=None):
        ct_pol = self.get_object(pk)
        s_ct_pol = CentroPoliesportivoSerializer(ct_pol)
        return Response(s_ct_pol.data)


    def update(self, request, pk, format=None):
        ct_pol = self.get_object(pk)
        s_ct_pol = CentroPoliesportivoSerializer(ct_pol, data=request.data)
        if s_ct_pol.is_valid():
            s_ct_pol.save()
            return Response(s_ct_pol.data)
        return Response(s_ct_pol.error, status=status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, format=None):
        ct_pol = self.get_object(pk)
        ct_pol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuadraRetrieveUpdateDestroy(APIView):
    def get_object(self, pk):
        try:
            quadra = Quadra.objects.get(pk=pk)
        except Quadra.DoesNotExist:
            raise Http404
        

    def get(self, request, pk, format=None):
        quadra = self.get_object(pk)
        s_quadra = QuadraSerializer(quadra)
        return Response(s_quadra.data)


    def update(self, request, pk, format=None):
        quadra = self.get_object(pk)
        s_quadra = QuadraSerializer(quadra, data=request.data)
        if s_quadra.is_valid():
            s_quadra.save()
            return Response(s_quadra.data)
        return Response(s_quadra.error, status=status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, format=None):
        quadra = self.get_object(pk)
        quadra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuxPartidaSerializersRetrieveUpdateDestroy(APIView):
    def get_object(self, pk):
        try:
            aux_part = AuxPartida.objects.get(pk=pk)
        except AuxPartida.DoesNotExist:
            raise Http404
        

    def get(self, request, pk, format=None):
        aux_part = self.get_object(pk)
        s_aux_part = AuxPartidaSerializer(aux_part)
        return Response(s_aux_part.data)


    def update(self, request, pk, format=None):
        aux_part = self.get_object(pk)
        s_aux_part = CentroPoliesportivoSerializer(aux_part, data=request.data)
        if s_aux_part.is_valid():
            s_aux_part.save()
            return Response(s_aux_part.data)
        return Response(s_aux_part.error, status=status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, format=None):
        aux_part = self.get_object(pk)
        aux_part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @csrf_exempt
@api_view(['GET', 'POST'])
def ctpol_list_create(request):
    if request.method == 'GET':
        return Response({"message": "fazendo ainda"})

    elif request.method == 'POST':
        data = json.loads(request.body)
        
        ct_pol_json = data.get('ct_pol')
        quadras_json = data.get('quadras')
        aux_partida_json = data.get('aux_partida')
        periodos_func_json = data.get('periodos_func')

        ctpol_info = {
            "nome": ct_pol_json.get('nome'),
            "cep": ct_pol_json.get('cep'),
            "numero": ct_pol_json.get('numero'),
            "quantidade_quadras": ct_pol_json.get('quantidade_quadras'),
            "contato_dono": ct_pol_json.get('contato_dono'),
            "descricao": ct_pol_json.get('descricao'),
            "avaliacao": 0
        }

        # cadastrando o ct
        s_ct_pol = CentroPoliesportivoSerializer(data=ctpol_info)
        if not s_ct_pol.is_valid():
            print("ERRO CTPOL")
            return Response(s_ct_pol.errors, status=status.HTTP_400_BAD_REQUEST)
        ct_pol = s_ct_pol.save()

        id_ct_pol = ct_pol.id


        # cadastrando as quadras do ct
        for i in range(int(ct_pol_json.get('quantidade_quadras'))):
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
        quantidade_aux_parts = len(aux_partida_json['modalidade'])
        for i in range(quantidade_aux_parts):
            aux_part = {
                "ct_pol": id_ct_pol,
                "modalidade": aux_partida_json['modalidade'][i],
                "quantidade_minima": aux_partida_json['quantidade_minima'][i],
                "valor_final": aux_partida_json['valor_final'][i],
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


        return Response({"status": "cadastrado com sucesso"}, status=status.HTTP_201_CREATED)

