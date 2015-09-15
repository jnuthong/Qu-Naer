# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0008_auto_20150411_1735'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='personalpost',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='personalpost',
            name='topic',
        ),
        migrations.DeleteModel(
            name='PersonalPost',
        ),
    ]
