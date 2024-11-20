from django.urls import path
from .views import RegisterView, loginView

urlpatterns = [
    path('login', loginView.as_view(), name="login"),
    # path('/token'),
    path('register', RegisterView.as_view(), name='registrar'),
    # path('/logout'),
]