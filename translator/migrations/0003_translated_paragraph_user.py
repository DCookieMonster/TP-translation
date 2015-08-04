# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('translator', '0002_auto_20150727_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='translated_paragraph',
            name='user',
            field=models.ForeignKey(default=1, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
