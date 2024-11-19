from django.urls import path, include
from .views import ModalidadeListCreate, ModalidadeRetrieveUpdateDestroy, CentroPoliesportivoListCreate, CentroPoliesportivoRetrieveUpdateDestroy, PeriodoFuncionamentoListCreate, PeriodoFuncionamentoRetrieveUpdateDestroy, QuadraListCreate, QuadraRetrieveUpdateDestroy, AuxPartidaListCreate, AuxPartidaSerializersRetrieveUpdateDestroy, ctpol_list_create, ctpol_detail, CidadeEstadoListCreate, CidadeEstadoRetrieveUpdateDestroy

urlpatterns = [
    path('modalidade/', ModalidadeListCreate.as_view(), name='modalidade-list-create'),
    path('modalidade/<int:pk>/', ModalidadeRetrieveUpdateDestroy.as_view(), name='modalidade-rud'),

    path('centro_poliesportivo/', CentroPoliesportivoListCreate.as_view(), name='centro_poliesportivo-list-create'),
    path('centro_poliesportivo/<int:pk>/', CentroPoliesportivoRetrieveUpdateDestroy.as_view(), name='centro_poliesportivo-rud'),

    path('periodo_funcionamento/', PeriodoFuncionamentoListCreate.as_view(), name='periodo_funcionamento-list-create'),
    path('periodo_funcionamento/<int:pk>/', PeriodoFuncionamentoRetrieveUpdateDestroy.as_view(), name='periodo_funcionamento-rud'),

    path('quadra/', QuadraListCreate.as_view(), name='quadra-list-create'),
    path('quadra/<int:pk>/', QuadraRetrieveUpdateDestroy.as_view(), name='quadra-rud'),

    path('aux_partida/', AuxPartidaListCreate.as_view(), name='aux_partida-list-create'),
    path('aux_partida/<int:pk>/', AuxPartidaSerializersRetrieveUpdateDestroy.as_view(), name='aux_partida-rud'),

    path('cidade_estado/', CidadeEstadoListCreate.as_view(), name='cidade_estado-list-create'),
    path('cidade_estado/<int:pk>/', CidadeEstadoRetrieveUpdateDestroy.as_view(), name='cidade_estado-rud'),
    
    path('ctpol_list_create/', view=ctpol_list_create, name='ctpol_list_create'),
    path('ctpol_detail/<int:pk>', view=ctpol_detail, name='ctpol_detail')
]    
