from django.db import models

class Usuario(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_nascimento = models.DateField()
