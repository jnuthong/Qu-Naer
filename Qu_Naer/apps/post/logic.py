#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '20/03/2014'

from utils.logger import error
from apps.post.models import Post


class PostLogic(object):
    @classmethod
    def get_one_post(cls, post_id):
        post_dict = Post.get_one_post(post_id).canonical_trim_post()
        return post_dict

    @classmethod
    def get_post_by_user_id(cls, user_id):
        try:
            post_list = Post.objects.filter(user_id=int(user_id), post_status=0)
            if len(post_list) > 0:
                return [element.id for element in post_list]
            else:
                return []
        except Exception as e:
            error(e)
            return []

    @classmethod
    def create_post(cls, **kwargs):
        try:
            post = Post.create_post(**kwargs)
            return post.canonical()
        except Exception as e:
            print('insert failed:%s' % str(e))
            return None

    @classmethod
    def update_post(cls, **kwargs):
        """
        Update post property base on the argument post_id
        """
        try:
            post_id = kwargs.pop('post_id')
            post = Post.get_one_post(post_id)
            if post and post.user_id == int(kwargs.pop('user_id')):
                for key, value in kwargs.items():
                    setattr(post, key, value)
                post.save()
                return post.canonical()
            else:
                raise Exception("No exist Post:post_id: %s" %post_id)
        except Exception as e:
            print(e)
            return 0

    @classmethod
    def delete_post(cls, post_id, user_id):
        post = Post.objects.get(post_id=post_id)
        if post is None:
            raise Exception(u'post_id is not exist')
        if user_id != post.user_id:
            raise Exception(u'not your post')
        post.post_status = 1
        post.save()
        return



