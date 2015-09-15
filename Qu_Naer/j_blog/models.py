# -*- encoding: utf-8 -*-
__author__ = "J Hong"
__date__ = "04/04/2015"
from django.db import models

# Create your models here.

# about how to query REF: https://docs.djangoproject.com/en/1.7/ref/models/querysets/#values-list

class PostTopic(models.Model):
    """
    """
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'rdb_post_topic'

    def __unicode__(self):
        return self.topic

    @classmethod
    def get_all_topic_m(cls):
        return PostTopic.objects.values_list('topic', flat=True).distinct()

class PersonalPost(models.Model):
    """
    """
    LANG_CHOICE = (
        ('cn', "Chinese"),
        ('en', "English"),
    )
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    author = models.CharField(max_length=32, blank=True, null=True)
    language = models.CharField(max_length=2,
                                choices=LANG_CHOICE,
                                default='en')
    title = models.CharField(max_length=128, null=True)
    topic = models.ForeignKey(PostTopic)
    index_time = models.CharField(max_length=16, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    post_status = models.SmallIntegerField(blank=True, null=True, help_text="1 for active, 0 for hidden")
    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rdb_personal_post'
        index_together = [
            ["author"],
            ["index_time"],
            ["title"],
            ["topic"],
            ["post_status"],
        ]

    def __unicode__(self):
        return self.content

    @classmethod
    def get_time_index_m(cls):
        return PersonalPost.objects.values_list('index_time',flat=True).distinct()