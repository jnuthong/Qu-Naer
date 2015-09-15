# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0006_auto_20150411_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.BigIntegerField(null=True, blank=True)),
                ('author', models.CharField(max_length=32, null=True, blank=True)),
                ('language', models.CharField(default=b'en', max_length=2, choices=[(b'cn', b'Chinese'), (b'en', b'English')])),
                ('title', models.CharField(max_length=128, null=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
                ('post_status', models.SmallIntegerField(null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('topic', models.ForeignKey(default=b'Normal', to='j_blog.PostTopic')),
            ],
            options={
                'db_table': 'rdb_personal_post',
            },
        ),
        migrations.AlterIndexTogether(
            name='personalpost',
            index_together=set([('author',), ('content',), ('topic',), ('post_status',)]),
        ),
    ]
