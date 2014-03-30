from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.core import cache
from django.contrib.auth.models import User
from utils.utils import *
import datetime
from django.utils.timezone import utc

class UserProfile(models.Model):
    user_id = models.AutoField(max_length=32, primary_key=True, unique=True)
    user_password = models.CharField(max_length=32, null=True)
    user_email = models.CharField(max_length=256, null=True)
    user_mobile = models.CharField(max_length=32, null=True)
    user_name = models.CharField(max_length=128, null=True)
    user_nick = models.CharField(max_length=128, null=True)
    login_type = models.SmallIntegerField(blank=True, null=True)
    register_time = models.DateTimeField(blank=True,
                                         null=True,
                                         auto_now_add=True)
    register_ip = models.CharField(max_length=20, null=True)
    last_login_time = models.DateTimeField(blank=True,
                                           null=True,
                                           default=datetime.datetime.utcnow().replace(tzinfo=utc))
    last_login_ip = models.CharField(max_length=20, null=True)
    user_image = models.CharField(max_length=32, null=True)
    real_name = models.CharField(max_length=32, null=True)
    sex = models.SmallIntegerField(blank=True, null=True) # 1-male; 0-female;
    birth_year = models.SmallIntegerField(blank=True, null=True)
    birth_month = models.SmallIntegerField(blank=True, null=True)
    birth_day = models.SmallIntegerField(blank=True, null=True)
    province = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)
    district = models.CharField(max_length=512, null=True)
    signature = models.CharField(max_length=512, null=True)
    third_key = models.CharField(max_length=512, null=True)
    third_type = models.SmallIntegerField(max_length=2, null=True)

    class Meta:
        db_table = 'rdb_user_profile'
        index_together = [
            ["user_id"],
            ["user_nick"],
            ["user_email"],
        ]

    @classmethod
    def create_user_profile(cls, **kwargs):
        """
        Create user profile by provided user_email, user_password, user_mobile, user_nick
        REQUIREMENT PARAM:
            - user_mobile/user_email, at least one param is required
            - user_password
            - user_nick
            - register_ip
            - sex
            - province (this is important)
            - city (important info)
            - district (should be provided)
        OPTIONAL PARAM:
            - another param is optional
        """
        if 'user_mobile' in kwargs.keys(): user_mobile = kwargs.get('user_mobile')
        else: user_mobile = None

        if 'user_email' in kwargs.keys(): user_email = kwargs.get('user_email')
        else: user_email = None

        if user_mobile == None and user_email == None:
            return dict(msg="Please provide user_mobile/user_email, at least one!")

        if user_mobile != None:
            user_obj = UserProfile(user_mobile=user_mobile,
                                   user_password=kwargs.get('user_password'),
                                   user_nick=kwargs.get('user_nick'),
                                   register_ip=kwargs.get('register_ip'),
                                   sex=kwargs.get('sex'),
                                   province=kwargs.get('province'),
                                   city=kwargs.get('city'),
                                   register_time=datetime.datetime.utcnow().replace(tzinfo=utc),
                                   last_login_time=datetime.datetime.utcnow().replace(tzinfo=utc),
                                   district=kwargs.get('district'))
            user_obj.save()
            return dict(msg="Success register with mobile phone number")
        elif user_email != None:
            user_obj = UserProfile(user_email=user_email,
                                   user_password=kwargs.get('user_password'),
                                   user_nick=kwargs.get('user_nick'),
                                   register_ip=kwargs.get('register_ip'),
                                   sex=kwargs.get('sex'),
                                   province=kwargs.get('province'),
                                   city=kwargs.get('city'),
                                   register_time=datetime.datetime.utcnow().replace(tzinfo=utc),
                                   last_login_time=datetime.datetime.utcnow().replace(tzinfo=utc),
                                   district=kwargs.get('district'))
            user_obj.save()
            return dict(msg="Success register with email")

    @classmethod
    def create_user_profile_by_third_user(cls, user_id, third_key, third_type):
        user_profile = UserProfile(user_id=user_id,
                                   third_key=third_key,
                                   third_type=third_type)
        user_profile.save()
        return user_profile

    @classmethod
    def get_user_profile_by_user_id(cls, user_id):
        try:
            return UserProfile.objects.get(user_id=user_id)
        except Exception as e:
            return dict(msg="Error in get user_profile!")

    @classmethod
    def check_nickname(cls, user_nick):
        """
        """
        try:
            obj = UserProfile.objects.get(user_nick=user_nick)
            return False # this nick name already exist
        except Exception as e:
            return True # this nick name is OK

    @classmethod
    def check_email(cls, user_email):
        """
        """
        try:
            obj = UserProfile.objects.get(user_email=user_email)
            return False # this email already exist
        except Exception as e:
            return True # this email is OK

    @classmethod
    def check_mobile(cls, user_mobile):
        """
        """
        try:
            obj = UserProfile.objects.get(user_mobile=user_mobile)
            return False # this user_mobile already exist
        except Exception as e:
            return True # this user_mobile is OK