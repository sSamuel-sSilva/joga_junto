from django.urls import path
from .views import UsuarioAgendamentoListCreate, UsuarioAgendamentoRetrieveUpdateDestroy, AgendamentoPartidaListCreate, AgendamentoPartidaRetrieveUpdateDestroy

urlpatterns = [
    path('usuario_agendamento/', UsuarioAgendamentoListCreate.as_view(), name='usuario_agendamento-list-create'),
    path('usuario_agendamento/<int:pk>/', UsuarioAgendamentoRetrieveUpdateDestroy.as_view(), name='usuario_agendamento-rud'),

    path('agendamento_partida/', AgendamentoPartidaListCreate.as_view(), name='agendamento_partida-list-create'),
    path('agendamento_partida/<int:pk>/', AgendamentoPartidaRetrieveUpdateDestroy.as_view(), name='agendamento_partida-rud'),

]  