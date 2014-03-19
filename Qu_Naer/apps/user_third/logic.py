from apps.user_third.models import UserThird

class UserThirdLogic(object):

    @classmethod
    def get_third_user_info(cls, third_key, third_type):
        try:
            user_third = UserThird.objects.get(third_key=third_key, third_type=third_type)
            return user_third
        except Exception as e:
            return None

    @classmethod
    def create_third_user(cls, user_id, third_key, third_type):
        return UserThird.objects.create(user_id=user_id, third_key=third_key, third_type=third_type)