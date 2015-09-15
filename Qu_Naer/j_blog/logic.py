# -*- encoding: utf-8 -*-

from j_blog.models import PostTopic, PersonalPost

class BlogLogic(object):
    """
    """

    @classmethod
    def get_all_topic_l(cls):
        """
        """
        return PostTopic.get_all_topic_m()

    @classmethod
    def get_time_index_l(cls):
        """
        """
        return PersonalPost.get_time_index_m()