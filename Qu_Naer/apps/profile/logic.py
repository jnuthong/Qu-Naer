# -*- encoding: utf-8 -*-
from apps.profile.models import UserProfile
from utils.logger import error

class UserProfileLogic(object):

    @classmethod
    def get_user_profile_by_user_id(cls, user_id):
        return UserProfile.get_user_profile_by_user_id(user_id=user_id)

    @classmethod
    def email_valid_checker_f(cls, email):
        """
        """
        if email is None: return False
        return UserProfile.check_email(email)

    @classmethod
    def active_account_f(cls, user_email, valid_code):
        """
        """
        if user_email is None or valid_code is None: return dict(msg="Error in function profile::logic::active_account_f(), either user_email or valid_code is none")
        return UserProfile.active_account_m(user_email=user_email,
                                            valid_code=valid_code)

    @classmethod
    def get_comments_by_user_id(cls, user_id):
        """
        Get whole comments list by user_id, Coded by J
        Not Finished Yet
        Note: this code is suspending for further using, because of feature of last app
        """
        try:
            pass
        except Exception as e:
            error(e)

    @classmethod
    def nickname_check(cls, user_nick):
        """
        REQUIRE_PARAM:
            user_nick
        return bool value, 0: you could use that, 1: ok, u can use
        """
        return UserProfile.check_nickname(user_nick)

    @classmethod
    def create_user_profile(cls, user_email, city_name, gender, register_ip, password):
        """
        """
        return UserProfile.create_user_profile(
            user_email=user_email,
            city_name=city_name,
            gender=gender,
            password=password,
            register_ip=register_ip)

    @classmethod
    def create_user_profile_by_third_user(cls, user_id, third_key, third_type):
        return UserProfile.create_user_profile_by_third_user(
            user_id=user_id,
            third_key=third_key,
            third_type=third_type
        )

    @classmethod
    def update_last_login_time(cls, user_id):
        ret = UserProfile.update_last_login_time(user_id)
        return ret

    @classmethod
    def update_user_profile(cls, user_id, user_nick, province, city, district, signature, user_image):
        user_profile =  UserProfile.update_user_profile(
            user_id=user_id,
            user_nick=user_nick,
            province=province,
            city=city,
            district=district,
            signature=signature,
            user_image=user_image
        )
        return user_profile

    @classmethod
    def update_user_profile_by_third_user(cls, user_id, user_nick, province, city, district, signature,
                                          user_image, register_ip, sex):
        return UserProfile.update_user_profile_by_third_user(
            user_id=user_id,
            user_nick=user_nick,
            province=province,
            city=city,
            district=district,
            signature=signature,
            user_image=user_image,
            register_ip=register_ip,
            sex=sex
        )