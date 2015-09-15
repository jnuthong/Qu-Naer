# -*- coding: utf-8 -*-
import sys, traceback
from django.shortcuts import render
from apps.profile.logic import UserProfileLogic
from ipware.ip import get_ip
from utils.utils import is_email, is_mobile_phone
from django.core.context_processors import csrf
from utils.utils import md5
# from django.views.decorators.csrf import csrf_protect

def register(request):
    """
    Product by J, quality promise
    REQUIRE_PARAM:
        - user_password
        - user_email
        - user_mobile
        - user_nick (this is should be unique)
        - register_ip
        - sex
        - province
        - city
        - district
        - register_ip: maintain var for statistic using, to compute the potential user
    """
    if request.method == "GET":
        return dict(msg="Unexpected request method!",
                    warn="OK")
    else:
        try:
            user_mobile = None
            user_email = None
            # if 'user_mobile' in request.POST.keys():
            #     user_mobile = request.POST.get('user_mobile')
            #
            #     if is_mobile_phone(int(user_mobile)): None
            #     else: return dict(msg="Un-correct format of mobile phone number")
            if "user_email" in request.POST.keys():
                user_email = request.POST.get('user_email')

                if is_email(user_email): None
                else: return dict(msg="Un-correct format of email",
                                  danger="OK")

            city_name = request.POST.get('city_name').encode("utf-8")
            gender = request.POST.get('gender').encode("utf-8")
            password = request.POST.get('user_password').encode("utf-8")
            c_password = request.POST.get('user_confirm_password').encode("utf-8")
            register_ip = get_ip(request)

            # print city_name, gender, password, c_password, register_ip, type(gender)
            if password != c_password:
                return dict(msg="Password is not same!", warn="OK")
            else: password = md5(password)

            return UserProfileLogic.create_user_profile(user_email=user_email,
                                                        city_name=city_name,
                                                        gender=gender,
                                                        password=password,
                                                        register_ip=register_ip)
        except Exception as e:
            print traceback.format_exc()
            return dict(msg="Error occur in user register: %s" % str(e),
                        danger="OK")

def nickname_check(request):
    """
    REQUIRE_PARAM:
        - user_nick:
    """
    if request.method == "GET":
        return dict(msg="Unexpected request method!")
    else:
        try:
            user_nick = request.POST.get('user_nick')
            return dict(result=UserProfileLogic.nickname_check(user_nick))
        except Exception as e:
            return dict(msg="Error in checking user nickname: %s" % str(e))

def validEmail(request):
    """
    REQUIRE_PARAM:
        - user_email:
    """
    if request.method == "POST":
        return dict(msg="Unexpected request method!",
                    warn="OK")
    else:
        try:
            user_email = request.GET.get('user_email')
            if is_email(user_email):
                return UserProfileLogic.email_valid_checker_f(user_email)
        except Exception as e:
            return dict(msg="Error in function profile::views::validEmail(), %s" % str(e),
                        warn="OK")

def signup(request):
    """
    """
    return render(request, 'signup.html', {})

def activeAccount(request):
    """
    """
    if request.method == "POST":
        return dict(msg="Unexpected request method!",
                    warn="OK")
    else:
        try:
            user_email = request.GET.get('user_email')
            valid_code = request.GET.get('valid_code')
            if is_email(user_email):
                return UserProfileLogic.active_account_f(user_email=user_email,
                                                         valid_code=valid_code)
        except Exception as e:
            return dict(msg="Error in function profile::views::activeAccount(), %s" % str(e),
                        warn="OK")

def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    main()