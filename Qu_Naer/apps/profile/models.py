from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.core import cache

class UserProfile(models.Model):
    user_id = models.BigIntegerField(max_length=32, blank=True)
    user_password = models.CharField(max_length=32, null=True)
    user_email = models.CharField(max_length=256, null=True)
    user_mobile = models.CharField(max_length=32, null=True)
    user_name = models.CharField(max_length=128, null=True)
    user_nick = models.CharField(max_length=128, null=True)
    login_type = models.SmallIntegerField(blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    register_ip = models.CharField(max_length=20, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=20, null=True)
    user_image = models.CharField(max_length=32, null=True)
    realname = models.CharField(max_length=32, null=True)
    sex = models.SmallIntegerField(blank=True, null=True)
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
        managed = True
        db_table = 't_user_profile'
        index_together = [
            ["user_id"],
        ]
    def canonical(self):
        doc = model_to_dict(self, fields=('user_id', 'user_name', 'user_nick', 'user_image', 'signature', 'realname',
                                          'birth_year', 'birth_month', 'birth_day', 'province', 'city', 'district',
                                          'sex'))
        return doc

    def canonical_normal(self):
        doc = model_to_dict(self, fields=('user_id', 'user_name', 'user_nick', 'user_image', 'signature', 'province',
            'city', 'district'))
        return doc

    @classmethod
    def create_user_profile(cls, user_id, user_password, user_email, user_mobile, user_nick,
                            register_ip, sex, province, city, district):
        user_profile = UserProfile()
        user_profile.user_id = user_id
        user_profile.user_password = md5(user_password)
        user_profile.user_email = user_email
        user_profile.user_mobile = user_mobile
        user_profile.user_name = user_nick
        user_profile.user_nick = user_nick
        user_profile.register_time = datetime_convert_current_timezone(timezone.now())
        user_profile.register_ip = register_ip
        user_profile.sex = sex
        user_profile.province = province
        user_profile.city = city
        user_profile.district = district
        user_profile.save()

    @classmethod
    def create_user_profile_by_third_user(cls, user_id, third_key, third_type):
        user_profile = UserProfile()
        user_profile.user_id = user_id
        user_profile.third_key = third_key
        user_profile.third_type = third_type
        user_profile.save()
        return user_profile
