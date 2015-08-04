# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='docx',
            field=models.FileField(upload_to=b'uploads/%Y/%m/', blank=True),
        ),
    ]
