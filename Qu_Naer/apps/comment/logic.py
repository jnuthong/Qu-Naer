#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '28/09/2015'

from apps.comment.models import Comment, Mark


class CommentLogic(object):
    """
    Logic for Comment
    """
    @classmethod
    def get_one_comment(cls, comment_id):
        comment_dict = Comment.get_one_comment(comment_id).canonical()
        return comment_dict

    @classmethod
    def get_comments_by_game(cls, game_id, page_num):
        try:
            if page_num < 1:
                raise Exception(u'Comment page number<1!')
            comment_id_list = Comment.get_comment_list(game_id, page_num)
            comment_dict_list = []
            if len(comment_id_list) > 0:
                for comment_id in comment_id_list:
                    comment_dict_list.append(Comment.get_one_comment(comment_id).canonical_trim_comment)
                return comment_dict_list
            else:
                return []
        except Exception as e:
            print e
            return []

#   @classmethod
#    def add_comment(cls, game_id, user_id):