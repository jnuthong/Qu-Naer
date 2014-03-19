# -*- coding: utf-8 -*-
# Author: J Block
# Date: 15/04/2013

from django.db import models
from django.utils.timezone import utc
import datetime

class MComment(models.Model):
    """
    Comment have foreign key for some specify post
    """
    user_id = models.BigIntegerField(blank=True, null=True, help_text='user id of commend')
    comment_content = models.CharField(max_length=CommentConstants.Comment_Length, blank=True, null=True)
    post_id = models.BigIntegerField(blank=True, null=True)
    post_user_id = models.BigIntegerField(blank=True, null=True)
    discuss_comment_id = models.BigIntegerField(blank=True, null=True)
    discuss_user_id = models.BigIntegerField(blank=True, null=True)
    comment_type = models.SmallIntegerField(blank=True, null=True, help_text='is this comment is a re-comment')
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    comment_source = models.SmallIntegerField(blank=True, default=int(CommentSource.XiuMeijia_APP),
                                              help_text='comment sent from app/web, default is app')
    comment_status = models.SmallIntegerField(blank=True)

    class Meta:
        db_table = 's_comment'
        ordering = ['user_id', '-update_time']
        index_together = [
            ["post_id", "comment_status"],
            ["user_id", "update_time", "comment_status"],
            ["post_user_id", "update_time", "comment_status"],
            ["discuss_user_id", "update_time", "comment_status"],
        ]

    def __repr__(self):
        return u"{uid = %d, cid=%d, post_id=%d}" % (self.user_id, self.pk, self.post_id)

    def save(self, *args, **kwargs):
        """
        save the change after you modify or create a new comment
        """
        if not self.create_time:
            self.create_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.update_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(MComment, self).save(*args, **kwargs)
        return self

    def update_by_comment_id(self):
        """
        """
        pass

    def read_by_comment_id(self):
        """
        """
        pass

    def delete_by_comment_id(self):
        """
        """
        pass