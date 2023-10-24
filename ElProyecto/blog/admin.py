from django.contrib import admin
from .models import Entidad, Comunicado

# Register your models here.

class EntidadAdmin (admin.ModelAdmin):

    readonly_fields = ( 'entidad','publicado_por','modificado_por')

    def save_model(self, request, obj , form, change):
        usuario = request.user
        entidad = Entidad.objects.filter(administrador=usuario).first()
        obj.entidad = entidad
        obj.publicado_por = usuario
        obj.modificado_por = usuario
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(EntidadAdmin, self).get_queryset(request)
        qs = qs.filter(publicado_por=request.user)
        return qs


admin.site.register(Entidad)
admin.site.register(Comunicado,EntidadAdmin)
