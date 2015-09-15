# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.BigIntegerField(null=True, blank=True)),
                ('author', models.CharField(max_length=20, null=True, blank=True)),
                ('language', models.CharField(default=b'en', max_length=2, choices=[(b'cn', b'Chinese'), (b'en', b'English')])),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
                ('post_status', models.SmallIntegerField(null=True, blank=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
