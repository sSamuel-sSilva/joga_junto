from django.urls import path
from .views import RegisterView, loginView, visualizar_perfil

urlpatterns = [
    path('login', loginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name='registrar'),
    path('visualizar_perfil', view=visualizar_perfil, name="perfil"),
]