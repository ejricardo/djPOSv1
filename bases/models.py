from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    usuario_modifica = models.IntegerField(blank=True, null=True)
    fecha_modifica = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

