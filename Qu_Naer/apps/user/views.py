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

@transaction.commit_on_success
def register(request):
    pass