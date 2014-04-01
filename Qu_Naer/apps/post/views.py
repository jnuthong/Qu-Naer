#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '17/03/2014'

from apps.post.logic import PostLogic
from apps.profile.logic import UserProfileLogic
from main.settings import DEBUG


def create_post(request):
    """
    create post
    """
    try:
        if request.method == "POST" or DEBUG is True:
            user_id = int(request.POST.get('user_id'))
            if user_id != request.user.id:
                raise Exception(u'wrong user id')
            place_id = request.POST.get('place_id', 0)
            post_content = request.POST.get('post_content', '')
            #post_image = request.POST.get('post_image')
            post_source = int(request.POST.get('post_source', 1))
            post_type = int(request.POST.get('post_type', 0))
            post_theme = request.POST.get('post_theme', "")
            #image = upload_image(request)
            #post_image = image['content']['file_id']
            #post_image_meta = image['content']['id']

            #todo: add check here or give the client information async
            #ret = SendPostTask.delay(user_id, place_id, post_content, post_image, post_source, post_type,post_status=0, post_audit=0)
            ret = PostLogic.create_post(user_id, place_id, post_content, post_image, post_source, post_type, post_image_meta,post_theme = post_theme)
            if ret is None:
                raise Exception(u'post_id not exist')
            ret = dict(code=1, content=ret)
        else:
            ret = dict(code=2002, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        import traceback
        traceback.print_exc()
        ret = dict(code=2002, msg=u"Internal error:%s" % str(e))
    return ret

def get_one_post(request):
    """
    get the post according to post_id
    """
    try:
        if request.method == "POST" or DEBUG is True:
            post_id = request.POST.get('post_id')
            #user_id = request.POST.get('user_id')
            rtn = dict()
            if post_id is None:
                raise Exception('parameter error')
            post_info = PostLogic.get_one_post(post_id=post_id)
            if post_info is None:
                raise Exception(u'post_id not exist')
            user_info = UserProfileLogic.get_user_profile_by_user_id(user_id=int(post_info.get('user_id')))
            user = dict(user=user_info)
            #rtn['image_info'] = ImageLogic.fetch_image_info_by_meta_id(meta_id=post_info.get('post_image_meta'))
            #rtn['like_num'] = SocialLogic.get_post_liker_num(int(post_id))
            #rtn['comment_num'] = CommentLogic.get_comments_count_from_post_id(int(post_id))
            #rtn['isLiked'] = like
            rtn.update(post_info)
            rtn.update(user)
            rtn['post_content'] = post_info['post_content']
            ret = dict(code=1, content=rtn)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        #import traceback
        #traceback.print_exc()
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret


def get_post_list_by_time(request):
    """
    get post list by time
    """
    try:
        if request.method == "POST" or DEBUG is True:
            pass
        else:
            pass
    except Exception as e:
        pass
