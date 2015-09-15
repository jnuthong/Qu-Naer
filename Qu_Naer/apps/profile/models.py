# -*- encoding: utf-8 -*-
# This code is writed by J
from __future__ import unicode_literals
from django.db import models
import django
from multiprocessing import Pool
from django.forms.models import model_to_dict
from django.utils import timezone
from django.core import cache
from django.contrib.auth.models import User
from utils.utils import *
import datetime
from utils import utils
from django.utils.timezone import utc


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    user_password = models.CharField(max_length=32, null=True)
    user_email = models.CharField(max_length=64, unique=True)
    user_mobile = models.CharField(max_length=32, null=True)
    user_name = models.CharField(max_length=128, null=True)
    user_nick = models.CharField(max_length=128, null=True)
    login_type = models.SmallIntegerField(blank=True, null=True)
    register_time = models.DateTimeField(blank=True,
                                         null=True,
                                         auto_now_add=True)
    register_ip = models.GenericIPAddressField()
    last_login_time = models.DateTimeField(blank=True,
                                           null=True,
                                           default=django.utils.timezone.now)
    last_login_ip = models.GenericIPAddressField()
    user_image = models.CharField(max_length=32, null=True)
    real_name = models.CharField(max_length=32, null=True)
    sex = models.TextField(null=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    birth_month = models.SmallIntegerField(blank=True, null=True)
    birth_day = models.SmallIntegerField(blank=True, null=True)
    province = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)
    district = models.CharField(max_length=512, null=True)
    signature = models.CharField(max_length=512, null=True)
    third_key = models.CharField(max_length=512, null=True)
    third_type = models.SmallIntegerField(null=True)

    valid_code = models.BinaryField(max_length=128, null=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'rdb_user_profile'
        index_together = [
            ["user_id"],
            ["user_nick"],
            ["user_email"],
        ]

    def __str__(self):
        return "%s, %s" % (self.user_id, self.user_email)

    def __unicode__(self):
        """
        """
        return "%s, %s" % (self.user_id, self.user_email)

    @classmethod
    def active_account_m(cls, **kwargs):
        """
        REQUIREMENT PARAM:
            - user_email:
            - valid_code:
        """
        try:
            user_email, valid_code = None, None
            if 'user_email' in kwargs.keys(): user_email = kwargs.get("user_email")
            if 'valid_code' in kwargs.keys(): valid_code = kwargs.get("valid_code")
            UserProfile.objects.filter(user_email=user_email,
                                       valid_code=valid_code).update(is_active=True)
            return True
        except Exception as e:
            return dict(msg="Error in function profile::models::active_account_m(), %s" % str(e),
                        danger="OK")

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

        if user_mobile is None and user_email is None:
            return dict(msg="Please provide user_mobile/user_email, at least one!",
                        msg_cn="请用正确的邮箱或电话注册!",
                        warn="OK")

        # if user_mobile is not None:
        #     user_obj = UserProfile(user_mobile=user_mobile,
        #                            user_password=kwargs.get('user_password'),
        #                            user_nick=kwargs.get('user_nick'),
        #                            register_ip=kwargs.get('register_ip'),
        #                            sex=kwargs.get('sex'),
        #                            province=kwargs.get('province'),
        #                            city=kwargs.get('city'),
        #                            register_time=datetime.datetime.utcnow().replace(tzinfo=utc),
        #                            last_login_time=datetime.datetime.utcnow().replace(tzinfo=utc),
        #                            district=kwargs.get('district'))
        #     user_obj.save()
        #     return dict(msg="Success register in mobile phone number")
        if user_email is not None and cls.check_email(user_email):
            valid_code = utils.random_bits(128)
            user_obj = UserProfile(user_email=user_email,
                                    user_password=kwargs.get('password'),
                                    register_ip=kwargs.get('register_ip'),
                                    last_login_ip=kwargs.get('register_ip'),
                                    sex=kwargs.get('gender'),
                                    valid_code=valid_code,
                                    city=kwargs.get('city_name'))
            user_obj.save()

            # send valid code
            msg = utils.html_template_wrapper("templates/mail/valid_template.html",
                                              "{{ link }}",
                                              settings.SITE_ADDRESS+"/activeAccount"+\
                                              "?validCode="+str(valid_code)+\
                                              "&user_email="+user_email)
            # print msg
            # pool = Pool(processes=1)
            # pool.apply_async(utils.send_email, [(user_email, "Account Active Link From" + settings.SITE_NAME)])
            # TODO here should add another asynchronize procedure [send active email]
            utils.send_email(user_email,
                             subject="Account Active Link From" + settings.SITE_NAME,
                             html_str=msg)
            return dict(msg="Success register in email, please check your email to active user!",
                        msg_cn="注册成功，请查收邮箱激活用户!",
                        result="OK")
        else:
            return dict(msg="Fail in register (email have been registered before), please contact the admin!",
                        msg_cn="注册失败 (邮箱已注册)，请联系管理员!",
                        result=None)

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
            if UserProfile.objects.get(user_email=user_email) is None: return True
            return False
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
