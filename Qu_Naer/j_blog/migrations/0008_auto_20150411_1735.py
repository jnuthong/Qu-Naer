# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0007_auto_20150411_1733'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='personalpost',
            index_together=set([('author',), ('title',), ('topic',), ('post_status',)]),
        ),
    ]
