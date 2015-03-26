# -*- coding: utf-8 -*-

from celery import task
from celery import current_app
from django.db import transaction
from textalytics import config
from lecciones.models import Etiquetar
from textalytics.SemPubClient import SemPubClient
from textalytics.SemPubException import SemPubException
from textalytics.Domain import Dictionary, Document

from utils import GMT1
import datetime



@task(ignore_result=True)
@transaction.commit_manually
def etiquetar():
    try:
        records = Etiquetar.objects.select_for_update(nowait=False).select_related('leccion', 'diccionario').filter(procesando=False, procesado=False)[:1]
        if records:
            gmt = GMT1()
            for record in records:
                Etiquetar.objects.filter(pk=record.pk).update(procesando=True, inicio=datetime.datetime.now())
                extra = {
                    "language": record.leccion.language,
                    "source": record.leccion.source,
                    "timeref": record.leccion.timeref.replace(tzinfo=gmt).strftime("%Y-%m-%d %I:%M:%S %Z"),
                    "itf": record.leccion.itf
                }
                document = Document(record.pk, record.leccion.txt)
                document.update(extra)
                dictionary = Dictionary(record.diccionario.name, record.diccionario.language, record.diccionario.description)
                current_app.send_task('tasks.tasks.process', (record.pk, document, dictionary))
    except Exception, e:
        transaction.rollback()
        print str(e)
    else:
        transaction.commit()


@task(ignore_result=True)
def process(id, document, dictionary):
    try:
        textalytics = SemPubClient(config.KEY)
        result = textalytics.analyzeDocument(document, dictionary)
        Etiquetar.objects.filter(pk=id).update(procesando=False, procesado=True, fin=datetime.datetime.now(), resultado=result)
        print result
    except SemPubException as e:
        print 'Error: ' + str(e)




        