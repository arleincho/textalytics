# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diccionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'skosh send at')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etiquetar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('procesando', models.BooleanField(default=False)),
                ('procesado', models.BooleanField(default=False)),
                ('procesado_en', models.DateTimeField(null=True, blank=True)),
                ('resultado', jsonfield.fields.JSONField(default=b'{}', null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'cuando se creo la relacion')),
                ('inicio', models.DateTimeField(null=True, blank=True)),
                ('fin', models.DateTimeField(null=True, blank=True)),
                ('diccionario', models.ForeignKey(to='lecciones.Diccionario')),
            ],
            options={
                'verbose_name_plural': 'etiquetar',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('txt', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('itf', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('timeref', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'skosh send at')),
            ],
            options={
                'verbose_name_plural': 'lecciones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='etiquetar',
            name='leccion',
            field=models.ForeignKey(to='lecciones.Leccion'),
            preserve_default=True,
        ),
    ]
