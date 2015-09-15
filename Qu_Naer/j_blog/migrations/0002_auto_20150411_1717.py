# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_blog', '0001_initial'),
    ]

    operations = [
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
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='personalpost',
            name='author',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterIndexTogether(
            name='personalpost',
            index_together=set([('author',), ('title',), ('content',), ('topic',), ('post_status',)]),
        ),
        migrations.AlterModelTable(
            name='personalpost',
            table='rdb_personal_post',
        ),
        migrations.AddField(
            model_name='personalpost',
            name='topic',
            field=models.ForeignKey(to='j_blog.PostTopic', null=True),
        ),
    ]
