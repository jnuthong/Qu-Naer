# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0002_auto_20150411_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalpost',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
    ]
