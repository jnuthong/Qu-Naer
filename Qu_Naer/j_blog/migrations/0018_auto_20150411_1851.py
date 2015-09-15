# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0017_auto_20150411_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalpost',
            name='index_time',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personalpost',
            name='post_status',
            field=models.SmallIntegerField(help_text=b'1 for active, 0 for hidden', null=True, blank=True),
        ),
        migrations.AlterIndexTogether(
            name='personalpost',
            index_together=set([('author',), ('index_time',), ('topic',), ('title',), ('post_status',)]),
        ),
    ]
