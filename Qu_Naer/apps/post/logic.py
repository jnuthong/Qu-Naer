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
    def create_post(cls, user_id, place_id, post_content, post_image, post_source, post_type, post_image_meta, post_status=0, post_audit=0,post_theme = None):
        try:
            post = Post.create_post(user_id, place_id, post_content, post_image, post_source, post_type ,post_image_meta, post_status=0, post_audit=0)
            #========need move to other py!!!!===============
            #RLatestPost.add_new_post_to_latest_list(post)
            #store logic
            if post.place_id:
                RRank.update_store_front_image_by_place_id(post.place_id,post.post_image)
            SImageMeta.update_object_id(post.post_image_meta,post.id, object_type = 0)
            if post_theme:
                theme_lis = post_theme.split('#')
                for theme_name in theme_lis:
                    if not theme_name or theme_name == ' ' :
                        continue
                    SThemePost.update_theme_post_by_theme_name(theme_name, post.id, post_image=post.post_image,post_image_meta = post.post_image_meta)
            RPost.update_most_recent_post(post.id,post.post_image_meta)
            #=======================
            return post.canonical()
        except Exception as e:
            print('insert failed:%s' % str(e))
            return None