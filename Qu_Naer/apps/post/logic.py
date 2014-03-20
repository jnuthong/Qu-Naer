#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '20/03/2014'

from apps.post.models import Post


class PostLogic(object):
    @classmethod
    def get_one_post(cls, post_id):
        post_dict = Post.get_one_post(post_id).canonical_trim_post()
        return post_dict
