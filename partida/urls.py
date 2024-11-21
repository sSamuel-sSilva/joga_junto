from django.urls import path
from .views import UsuarioAgendamentoListCreate, UsuarioAgendamentoRetrieveUpdateDestroy, AgendamentoPartidaListCreate, AgendamentoPartidaRetrieveUpdateDestroy, cadastrar_listar_partida, partida_detalhe

urlpatterns = [
    path('usuario_agendamento/', UsuarioAgendamentoListCreate.as_view(), name='usuario_agendamento-list-create'),
    path('usuario_agendamento/<int:pk>/', UsuarioAgendamentoRetrieveUpdateDestroy.as_view(), name='usuario_agendamento-rud'),

    path('agendamento_partida/', AgendamentoPartidaListCreate.as_view(), name='agendamento_partida-list-create'),
    path('agendamento_partida/<int:pk>/', AgendamentoPartidaRetrieveUpdateDestroy.as_view(), name='agendamento_partida-rud'),

    path('agendar_buscar_partida/', view=cadastrar_listar_partida, name='cadastrar_partida'),
    path('partida_detalhada/<int:id>', view=partida_detalhe, name='ver_partida')
]  