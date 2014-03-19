from django.contrib.auth import login as auth_login, authenticate, logout as user_logout
from utils.utils import *
from apps.user.logic import SUserLogic
from apps.profile.logic import UserProfileLogic
from django.db import transaction

def login(request):
    if request.method == 'GET':
        return response_fail_to_mobile(500, REQUEST_METHOD_ERROR)
    try:
        username = request.POST['username']
        password = request.POST['password']

        if is_mobile_phone(username):
            user = authenticate(username=username, password=password, type=2)
        elif is_email(username):
            user = authenticate(username=username, password=password, type=1)
        else:
            raise Exception('Request params error')
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
        user_logout(request)
        return response_fail_to_mobile(500, "User_name or password is not right!")


def logout(request):
    if request.method == 'GET':
        return response_fail_to_mobile(500, REQUEST_METHOD_ERROR)
    try:
        user_logout(request)
        return response_success_to_mobile("Success in log!")
    except Exception as e:
        return response_fail_to_mobile(500, "Fail in log in!")


def update_user_info(request):
    if request.method == 'GET':
        return response_fail_to_mobile(500, REQUEST_METHOD_ERROR)
    try:
        id = request.POST['user_id']
        nick_name = request.POST['nick_name']
        province = request.POST['province']
        city = request.POST['city']
        district = request.POST['district']
        signature = request.POST['signature']
        user_image = request.POST['user_image']

        profile_logic = UserProfileLogic.update_user_profile(user_id=id,
                                                             user_nick=nick_name,
                                                             province=province,
                                                             city=city,
                                                             district=district,
                                                             signature=signature,
                                                             user_image=user_image)
        if profile_logic is None:
            raise Exception('Update user info error')
        return response_success_to_mobile('Success in updating user info')
    except Exception as e:
        return response_fail_to_mobile(500, 'Fail in updating user info')


@transaction.commit_manually
def register(request):
    if request.method == 'GET':
        return response_fail_to_mobile(500, REQUEST_METHOD_ERROR)
    try:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        nickname = request.POST['nickname']
        province = request.POST['province']
        city = request.POST['city']
        district = request.POST['district']
        sex = request.POST['sex']
        if password1 != password2:
            return response_fail_to_mobile(500, '注册失败')
        print('username:%s, password:%s' % (username, password1))
        if is_email(username):
            if SUserLogic.get_user_by_email(email=username):
                return response_fail_to_mobile(500, '注册失败,用户名已存在')
            logic = SUserLogic.create_user(username=username,
                                           email=username,
                                           mobile_phone=None,
                                           password=password1)
            if logic is None:
                raise Exception('Create user fail')
            UserProfileLogic.create_user_profile(user_id=logic.id,
                                                 user_password=password1,
                                                 user_email=username,
                                                 user_mobile=None,
                                                 user_nick=nickname,
                                                 register_ip=None,
                                                 sex=sex,
                                                 province=province,
                                                 city=city,
                                                 district=district)
        elif is_mobile_phone(username):
            if SUserLogic.get_user_by_mobile_phone(mobilephone=username):
                return response_fail_to_mobile(500, 'Fail in registering, user name alread exist!')
            logic = SUserLogic.create_user(username=username, email=None, mobile_phone=username, password=password1)
            if logic is None :
                raise Exception('Create user fail')
            UserProfileLogic.create_user_profile(user_id=logic.id,
                                                 user_password=password1,
                                                 user_email=None,
                                                 user_mobile=username,
                                                 user_nick=nickname,
                                                 register_ip=None,
                                                 sex=sex,
                                                 province=province,
                                                 city=city,
                                                 district=district)
        else:
            raise Exception('Request params error')
        return response_success_to_mobile("Success in registering!")
    except Exception as e:
        ret = response_fail_to_mobile(500, "Fail in registering!")
        transaction.rollback()
    finally:
        transaction.commit()
    return ret