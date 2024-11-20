from django.urls import path
from .views import RegisterView

urlpatterns = [
    # path('/login'),
    # path('/token'),
    path('register', RegisterView.as_view(), name='registrar'),
    # path('/logout'),
]