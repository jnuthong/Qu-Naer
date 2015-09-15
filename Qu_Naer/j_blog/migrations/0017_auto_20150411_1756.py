# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0016_auto_20150411_1742'),
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
            ],
            options={
                'db_table': 'rdb_personal_post',
            },
        ),
        migrations.CreateModel(
            name='PostTopic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('topic', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'db_table': 'rdb_post_topic',
            },
        ),
        migrations.AddField(
            model_name='personalpost',
            name='topic',
            field=models.ForeignKey(to='j_blog.PostTopic'),
        ),
        migrations.AlterIndexTogether(
            name='personalpost',
            index_together=set([('author',), ('title',), ('topic',), ('post_status',)]),
        ),
    ]
