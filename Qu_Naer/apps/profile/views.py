from apps.profile.logic import UserProfileLogic
from utils.utils import is_email, is_mobile_phone

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
        return dict(msg="Unexpected request method!")
    else:
        try:
            user_mobile = None
            user_email = None
            if 'user_mobile' in request.POST.keys():
                user_mobile = request.POST.get('user_mobile')

                if is_mobile_phone(int(user_mobile)): None
                else: return dict(msg="Un-correct format of mobile phone number")

            if 'user_email' in request.POST.keys():
                user_email = request.POST.get('user_email')

                if is_email(user_email): None
                else: return dict(msg="Un-correct format of email")

            password = request.POST.get('password')
            nickname = request.POST.get('user_nick')
            city = request.POST.get('city')
            district = request.POST.get('district')
            sex = request.POST.get('sex')
            province = request.POST.get('province')
            register_ip = request.POST.get('register_ip')
            return UserProfileLogic.create_user_profile(user_email=user_email,
                                                        user_mobile=user_mobile,
                                                        user_nick=nickname,
                                                        user_password=password,
                                                        city=city,
                                                        district=district,
                                                        sex=sex,
                                                        province=province,
                                                        register_ip=register_ip)
        except Exception as e:
            return dict(msg="Error occur in user register: %s" % str(e))

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
