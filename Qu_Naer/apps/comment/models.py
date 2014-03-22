# -*- coding: utf-8 -*-
# Author: J Hong
# Date: 15/04/2013

from django.db import models
from django.forms.models import model_to_dict
from django.utils.timezone import utc
import datetime

Comment_Length = 3000

class MComment(models.Model):
    """
    Comment have foreign key for some specify post
    """
    user_id = models.BigIntegerField(blank=True, null=False, help_text='user id of commend')
    comment_content = models.CharField(max_length=Comment_Length, blank=True, null=True)
    post_id = models.BigIntegerField(blank=True, null=False)
    post_user_id = models.BigIntegerField(blank=True, null=False)
    discuss_comment_id = models.BigIntegerField(blank=True, null=True)
    discuss_user_id = models.BigIntegerField(blank=True, null=True)
    comment_type = models.SmallIntegerField(blank=True, null=True, help_text='is this comment is a re-comment')
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    comment_source = models.SmallIntegerField(blank=True, default=0,
                                              help_text='comment sent from app/web, default is app')
    comment_status = models.SmallIntegerField(blank=True)

    class Meta:
        db_table = 'rdb_comment'
        ordering = ['user_id', '-update_time']
        index_together = [
            ["post_id", "comment_status"],
            ["user_id", "update_time", "comment_status"],
            ["post_user_id", "update_time", "comment_status"],
            ["discuss_user_id", "update_time", "comment_status"],
        ]

    def save(self, *args, **kwargs):
        """
        save the change after you modify or create a new comment
        """
        if not self.create_time:
            self.create_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.update_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(MComment, self).save(*args, **kwargs)
        return self

    def update_by_comment_id(self, *arg, **kwargs):
        """
        Update the comment content by comment id
        """
        if 'comment_content' in kwargs.keys():
            self.comment_content = kwargs.get('comment_content')
        self.save()
        return self


    def read_by_comment_id(self, *arg, **kwargs):
        """
        Query a comment by comment id, this default dict could change in the further base on the requirement
        """
        return model_to_dict(self, fields=['user_id',
                                           'comment_content',
                                           'post_id',
                                           'create_time',
                                           'update_time',
                                           'discuss_comment_id',
                                           'discuss_user_id'])

    def delete_by_comment_id(self, *arg, **kwargs):
        """
        Delete a comment by comment id, here use hard delete, which mean real delete, please care with this operation
        """
        try:
            self.delete()
        except Exception as e:
            return dict(msg="Error in delete comment:comment_id: , error msg: %s" % str(e))