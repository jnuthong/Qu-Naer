#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '17/03/2014'

from apps.post.logic import PostLogic
from main.settings import DEBUG

def get_one_post(request):
    """
    get the post according to post_id
    """
    try:
        if request.method == "POST" or DEBUG is True:
            post_id = request.POST.get('post_id')
            user_id = request.POST.get('user_id')
            rtn = dict()
            if post_id is None:
                raise Exception('parameter error')
            post_info = PostLogic.get_one_post(post_id=post_id)
            if post_info is None:
                raise Exception(u'post_id not exist')
            user_info = UserProfileLogic.get_compact_user_profile_by_user_id(user_id=int(post_info.get('user_id')))
            user = dict(user=user_info)
            theme = get_themes_by_post_id(post_id=post_id)
            #rpcret['image_info'] = ImageLogic.fetch_image_info(post_id,file_id=post_info.get('post_image'))
            rpcret['image_info'] = ImageLogic.fetch_image_info_by_meta_id(meta_id=post_info.get('post_image_meta'))
            rpcret['like_num'] = SocialLogic.get_post_liker_num(int(post_id))
            rpcret['comment_num'] = CommentLogic.get_comments_count_from_post_id(int(post_id))
            rpcret['isLiked'] = like
            rpcret.update(post_info)
            rpcret.update(user)
            rpcret.update(theme)
            rpcret['post_content'] = post_info['post_content']
            ret = dict(code=1, content=rpcret)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        import traceback
        traceback.print_exc()
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret