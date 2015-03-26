from django.db import models
from jsonfield import JSONField
import datetime
# Create your models here.


class Diccionario(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    created = models.DateTimeField('skosh send at', auto_now_add=True)

    def __str__(self):

        return self.name



class Leccion(models.Model):
    txt = models.TextField()
    language = models.CharField(max_length=100)
    itf = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    timeref = models.DateTimeField()
    created = models.DateTimeField('skosh send at', auto_now_add=True)

    class Meta:
        verbose_name_plural = "lecciones"

    def __str__(self):
        return self.txt


class Etiquetar(models.Model):
    leccion = models.ForeignKey(Leccion, blank=False, null=False)
    diccionario = models.ForeignKey(Diccionario, blank=False, null=False)
    procesando = models.BooleanField(default=False, blank=False, null=False)
    procesado = models.BooleanField(default=False, blank=False, null=False)
    resultado = JSONField(default='{}', null=True, blank=False)
    created = models.DateTimeField('cuando se creo la relacion', auto_now_add=True)
    inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)


    class Meta:
        verbose_name_plural = "etiquetar"

    def __str__(self):
        return "{0} {1} {2}".format(self.leccion, self.diccionario, self.procesado)
