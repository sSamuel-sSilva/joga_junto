from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_ctpol/', include('centro_poliesportivo.urls')),
    path('api_partida/', include('partida.urls')),
    path('auth/', include('usuario.urls')),
]
