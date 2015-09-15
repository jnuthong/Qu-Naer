# -*- encoding: utf-8 -*-
from utils.json_functions import json_view
from utils.utils import *
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from apps.profile.logic import UserProfileLogic
from apps.user_third.logic import UserThirdLogic
from django.db import transaction
from utils.logger import error

# @transaction.commit_manually
def check_third_user_is_exist(request):
    """
    Checked if the third user exist
    @param request: third_key, third_type
    @return: {exist_code:-1(未注册) 其他表示已经注册}
    """
    # if request.method == 'GET':
    #     return response_fail_to_mobile(500, REQUEST_METHOD_ERROR)
    # try:
    #     third_key = request.POST['third_key']
    #     third_type = request.POST['third_type']
    #
    #     logic = UserThirdLogic.get_third_user_info(third_key=third_key, third_type=third_type)
    #     if logic is not None:
    #         return dict(code=1, exist_code=1, content='This User have been registered')
    #     s_logic = SUserLogic.get_user_info_by_third(third_key=third_key, third_type=third_type)
    #     if s_logic is not None:
    #         raise Exception('The database table has it')
    #
    #     user_logic = SUserLogic.create_user_for_third(third_key=third_key, third_type=third_type)
    #
    #     UserProfileLogic.create_user_profile_by_third_user(user_id=user_logic.id, third_key=user_logic.third_key,
    #                                                        third_type=user_logic.third_type)
    #
    #     UserThirdLogic.create_third_user(user_id=user_logic.id, third_key=user_logic.third_key,
    #                                      third_type=user_logic.third_type)
    #     return dict(code=1, exist_code=-1, content='用户未注册')
    # except Exception as e:
    #     error(e)
    #     transaction.rollback()
    #     ret = response_fail_to_mobile(500, '检查第三方用户出错')
    # finally:
    #     transaction.commit()
    # return ret
    pass


def update_third_user_info(request):
    """
    The third user register
    @param request:sex, username, third_key, user_image, third_type, signature, register_ip,
        province, city, district
    @return:
    """
    if request.method == 'GET':
        return response_fail_to_mobile(500, REQUEST_METHOD_ERROR)
    try:
        third_key = request.POST['third_key']
        third_type = request.POST['third_type']
        username = request.POST['username']
        sex = request.POST['sex']
        user_image = request.POST['user_image']
        signature = request.POST['signature']
        register_ip = request.POST['register_ip']
        province = request.POST['province']
        city = request.POST['city']
        district = request.POST['district']

        third_logic = UserThirdLogic.get_third_user_info(third_key=third_key, third_type=third_type)

        if third_logic is None:
            return response_fail_to_mobile(1500, '修改第三方用户失败')

        profile_logic = UserProfileLogic.update_user_profile_by_third_user(user_id=third_logic.user_id,
                                                                           user_nick=username,
                                                                           province=province,
                                                                           city=city,
                                                                           district=district,
                                                                           signature=signature,
                                                                           user_image=user_image,
                                                                           register_ip=register_ip,
                                                                           sex=sex)
        if profile_logic is None:
             raise Exception('Update third user fail')
        return response_success_to_mobile('修改成功')
    except Exception as e:
        error(e)
        return response_fail_to_mobile(500, '修改第三方用户失败')



def third_user_login(request):

    """
    The method is third user login
    @param request: third_key, third_type
    @return:
    """
    if request.method == 'GET':
        return response_fail_to_mobile(500, REQUEST_METHOD_ERROR)
    try:
        username = request.POST['third_key']
        password = request.POST['third_type']
        user = authenticate(username=username, password=password, type=3)
        auth_login(request, user)
        logic = UserProfileLogic.get_user_profile_by_user_id(user_id=request.user.id)

        last_login = datetime_convert_current_timezone(logic.last_login_time)
        if last_login is not None:
            last_login = datetime_to_string(last_login)
        if logic.user_nick is None:
            user_nick = ''
        else:
            user_nick = logic.user_nick

        rec = dict()
        rec['session_id'] = request.session._session_key
        rec['user_id'] = request.user.id
        rec['user_name'] = user_nick
        rec['last_login'] = last_login
        UserProfileLogic.update_last_login_time(request.user.id)
        return response_success_to_mobile(rec)
    except Exception as e:
        error(e)
        auth_logout(request)
        return response_fail_to_mobile(500, 'Third part account login fail!')
