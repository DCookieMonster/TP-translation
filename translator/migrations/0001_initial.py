# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(unique=True, max_length=150)),
                ('docx', models.FileField(upload_to=b'', blank=True)),
                ('userId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('txt', models.TextField()),
                ('paperId', models.ForeignKey(to='translator.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Translated_Paragraph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('txt', models.TextField()),
                ('paraId', models.ForeignKey(to='translator.Paragraph')),
            ],
        ),
    ]
