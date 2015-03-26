from django.contrib import admin
from import_export.admin import ImportMixin
from lecciones.models import *
from lecciones.resources import LeccionResource
from lecciones.resources import DiccionarioResource
from django import forms


class DiccionarioAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = DiccionarioResource
    list_display = ('name', 'language', 'description')



class EtiquetarForm(forms.ModelForm):
 
    class Meta:
        model = Etiquetar
        fields = ['leccion', 'diccionario']



class EtiquetarAdmin(admin.ModelAdmin):
    form = EtiquetarForm
    list_display = ('leccion', 'diccionario', 'procesando', 'procesado', 'fin')
    # list_filter = ('procesado', 'procesado_en')




class LeccionesForm(forms.ModelForm):
    txt = forms.CharField(widget=forms.Textarea)
 
    class Meta:
        model = Leccion
        fields = ['txt', 'language', 'itf', 'source', 'timeref']



class LeccionAdmin(ImportMixin, admin.ModelAdmin):
    form = LeccionesForm
    resource_class = LeccionResource
    list_display = ('txt', 'language', 'itf', 'source', 'timeref')




admin.site.register(Etiquetar, EtiquetarAdmin)
admin.site.register(Diccionario, DiccionarioAdmin)
admin.site.register(Leccion, LeccionAdmin)