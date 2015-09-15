# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0012_auto_20150411_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalpost',
            name='topic',
            field=models.ForeignKey(default=b'0', to='j_blog.PostTopic'),
        ),
    ]
