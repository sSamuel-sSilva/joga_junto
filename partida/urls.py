from django.urls import path
from .views import UsarioAgendamentoListCreate, UsarioAgendamentoRetrieveUpdateDestroy, UsarioListCreate, UsarioRetrieveUpdateDestroy, AgendamentoPartidaListCreate, AgendamentoPartidaRetrieveUpdateDestroy, cadastrar_partida

urlpatterns = [
    path('usuario_agendamento/', UsarioAgendamentoListCreate.as_view(), name='usuario_agendamento-list-create'),
    path('usuario_agendamento/<int:pk>/', UsarioAgendamentoRetrieveUpdateDestroy.as_view(), name='usuario_agendamento-rud'),

    path('usuario/', UsarioListCreate.as_view(), name='usuario-list-create'),
    path('usuario/<int:pk>/', UsarioRetrieveUpdateDestroy.as_view(), name='usuario-rud'),

    path('agendamento_partida/', AgendamentoPartidaListCreate.as_view(), name='agendamento_partida-list-create'),
    path('agendamento_partida/<int:pk>/', AgendamentoPartidaRetrieveUpdateDestroy.as_view(), name='agendamento_partida-rud'),

    path('cadastrar_partida/<int:id>/', view=cadastrar_partida, name="cadastrar_partida")
]  