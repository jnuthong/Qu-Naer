#!/usr/bin/env python
#!-*-coding:utf-8-*-
__author__ = 'gong'
__create_time__ = '22/09/2015'

from django.db import models
from django.forms.models import model_to_dict
from django.utils.timezone import utc
import datetime

Comment_Length = 3000


class Comment(models.Model):
    """
    Comment have foreign key for some specify post
    """
    comment_id = models.AutoField(primary_key=True)
    game_id = models.BigIntegerField(blank=True, null=False)
    user_id = models.BigIntegerField(blank=True, null=False)
    score = models.PositiveSmallIntegerField(blank=False, null=False)
    comment_content = models.CharField(max_length=Comment_Length, blank=True, null=True)
    game_picture = models.CharField(max_length=128, blank=True, null=True)
    reply_comment_id = models.BigIntegerField(blank=True, null=True)
    reply_user_id = models.BigIntegerField(blank=True, null=True)
    reply_flag = models.SmallIntegerField(blank=True, null=True, help_text='is this comment is a re-comment')
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    comment_source = models.SmallIntegerField(blank=True, default=0,
                                              help_text='comment sent from app/web, default is app')
    comment_status = models.SmallIntegerField(blank=True)

    class Meta:
        db_table = 'rdb_comment'
        managed = True

    @classmethod
    def save(cls, *args, **kwargs):
        """
        save the change after you modify or create a new comment
        """
        if not cls.create_time:
            cls.create_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        cls.update_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Comment, cls).save(*args, **kwargs)
        return cls

    @classmethod
    def update_by_comment_id(cls, *arg, **kwargs):
        """
        Update the comment content by comment id
        """
        if 'comment_content' in kwargs.keys():
            cls.comment_content = kwargs.get('comment_content')
        cls.save()
        return cls

    @classmethod
    def get_comment_list(cls, game_id, page_num):
        offset = (page_num-1)*9
        limit = offset + 9
        ret = []
        qs = []
        try:
            qs = cls.objects.filter(game_id=game_id)[offset:limit]
        except Exception as e:
            print('get_comment_list error : %s' % str(e))
        for comment in qs:
            ret.append(comment.comment_id)
        return ret

    @classmethod
    def get_one_comment(cls, comment_id):
        """
        Query a comment by comment id, this default dict could change in the further base on the requirement
        """
        return cls.objects.filter(comment_id=comment_id)

    @classmethod
    def delete_by_comment_id(cls, comment_id):
        """
        Delete a comment by comment id, here use hard delete, which mean real delete, please care with this operation
        """
        try:
            cls.objects.filter(comment_id=comment_id).update(comment_status=1)
        except Exception as e:
            return dict(msg="Error in delete comment:comment_id: , error msg: %s" % str(e))


class Mark(models.Model):
    """
    Mark model for games
    """
    mark_id = models.AutoField(primary_key=True)
    game_id = models.BigIntegerField(blank=True, null=False)
    score = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'rdb_mark'
        managed = True

    @classmethod
    def save(cls, *args, **kwargs):
        """
        save the change after you modify or create a new comment
        """
        super(Mark, cls).save(*args, **kwargs)
        return cls

    @classmethod
    def get_by_game_id(cls, game_id):
        return cls.objects.get(game_id=game_id)

