#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '10/03/2014'


import datetime
#import zlib
from django.db import models
from django.forms.models import model_to_dict
from django.utils.timezone import utc

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    book_id = models.BigIntegerField(blank=True, null=True)
    place_id = models.BigIntegerField(blank=True, null=True)
    post_content = models.BinaryField(blank=True, null=True)    # without compress, todo: add compress content method
    post_image = models.CharField(max_length=32, blank=True)
    post_source = models.SmallIntegerField(blank=True, null=True)
    post_type = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    post_status = models.SmallIntegerField(blank=True, null=True)
    post_audit = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rdb_post'
        managed = True

    def __str__(self):
        return '%s, %s, %s, %s' % (self.id, self.user_id, self.book_id, self.place_id)

    def canonical(self):
        """
        return the object as a tuple
        """
        fields = model_to_dict(self, fields=('id', 'user_id', 'book_id', 'place_id', 'post_content', 'post_image',
                                             'post_source', 'post_type', 'create_time', 'update_time',
                                             'post_status', 'post_audit', 'post_image_meta'))
        return fields

    def canonical_trim_post(self):
        """
        trim post information for one post
        """
        fields = model_to_dict(self, fields=('id', 'user_id', 'place_id', 'post_content', 'create_time','post_image','post_image_meta'))
        post_id = fields.pop('id')
        fields['post_content'] = self.content
        fields['post_id'] = post_id
        time = fields.pop('create_time').strftime('%Y-%m-%d %H:%M:%S.000000+00:00')
        fields['create_time'] = time
        return fields

    def create_post(self, *args, **kwargs):
        if not self.create_time:
            self.create_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.update_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Post, self).save(*args, **kwargs)
        return self

    def get_one_post(self, post_id):
        return self.objects.get(id=post_id)

    def get_posts_by_user(self, user_id):
        return self.objects.filter(user_id=user_id)

    def update_post(self, post_id, **kwargs):
        self.objects.filter(id=post_id).update(**kwargs)

    def delete_post(self, post_id):
        self.objects.filter(id=post_id).update(post_status=1)


class SharedPost(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.BigIntegerField(blank=True, null=False)
    user_id = models.BigIntegerField(blank=True, null=False)
    create_time = models.DateTimeField(blank=True, null=False)

    class Meta:
        db_table = 'rdb_shard_post'
        managed = True

