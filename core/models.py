from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Assinante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plano = models.CharField(max_lenght=255)
    data_inicio_assinatura = models.DateField()
    data_fim_assinatura = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
class Produto(models.Model):
    descricao = models.CharField(max_lenght=255)
    cliente = models.ForeignKey(Assinante, on_delete=models.CASCADE)
