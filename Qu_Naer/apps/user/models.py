from __future__ import unicode_literals
import re
from django.core import validators
from django.contrib.auth.models import (
    UserManager,
    )

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser, BaseUserManager
from apps.user.manager import CustomeUserManager
from utils.utils import *

class SUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    mobilephone = models.CharField(null=True, db_index=True, max_length=128)
    full_name = models.CharField(null=True, max_length=128)
    short_name = models.CharField(null=True, max_length=128)
    third_key = models.CharField(null=True, max_length=128)
    third_type = models.SmallIntegerField(null=True, max_length=4)
    objects = CustomeUserManager()

    class Meta:
        db_table = 'rdb_user_account'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sms_user(self, subject, message, from_phone=None):
        """

        @param subject:
        @param message:
        @param from_phone:
        @raise NotImplementedError:
        """
        raise NotImplementedError

    @classmethod
    def get_user_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except Exception:
            return None

    @classmethod
    def get_user_by_mobile_phone(cls, mobilephone):
        try:
            return cls.objects.get(mobilephone=mobilephone)
        except Exception:
            return None

    def set_password(self, password):
        self.password = md5(password)

    def check_password(self, password):
        if self.password == md5(password):
            return True
        else:
            return False