from apps.user.models import SUser

class SUserLogic(object):

    @classmethod
    def get_user_info_by_third(cls, third_key, third_type):
        try:
            return SUser.objects.get(third_key=third_key, third_type=third_type)
        except Exception:
            return None

    @classmethod
    def create_user_for_third(cls, third_key, third_type):
        return SUser.objects.create(username=third_key + '_' + third_type,
                                    third_key=third_key,
                                    third_type=third_type)

    @classmethod
    def create_user(cls, username, email, mobile_phone, password):
        return SUser.objects.create_user(username=username,
                                         email=email,
                                         password=password,
                                         mobilephone=mobile_phone)

    @classmethod
    def get_user_by_email(cls, email):
        return SUser.get_user_by_email(email)

    @classmethod
    def get_user_by_mobile_phone(cls, mobilephone):
        return SUser.get_user_by_mobile_phone(mobilephone=mobilephone)