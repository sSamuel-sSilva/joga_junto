from django.urls import path, include
from .views import ModalidadeListCreate, ModalidadeRetrieveUpdateDestroy, CentroPoliesportivoListCreate, CentroPoliesportivoRetrieveUpdateDestroy, PeriodoFuncionamentoListCreate, PeriodoFuncionamentoRetrieveUpdateDestroy, QuadraListCreate, QuadraRetrieveUpdateDestroy, AuxPartidaListCreate, AuxPartidaSerializersRetrieveUpdateDestroy, cadastrar_ct_pol

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

    path('rotateste', cadastrar_ct_pol)
]    
