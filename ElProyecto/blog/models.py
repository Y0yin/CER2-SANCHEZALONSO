from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

TIPO_CHOICES=[
    ("S", "Suspensión de actividades"),
    ("C", "Suspensión de clase"),
    ("I", "Información"),]

class Entidad(models.Model):
    id= models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=150)
    logo= models.ImageField()
    administrador = models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    def __str__(self) -> str:
        return self.nombre
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"

class Comunicado(models.Model):
    id= models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=150)
    detalle= models.CharField(max_length=150)
    detalle_corto= models.CharField(max_length=60)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    entidad= models.ForeignKey(Entidad,null=True ,on_delete=models.CASCADE)
    visible= models.BooleanField(default=False) 
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificación= models.DateTimeField(auto_now=True)
    publicado_por= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, related_name='comunicado_publicado', on_delete=models.CASCADE)
    modificado_por= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, related_name='comunicado_modificado',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo