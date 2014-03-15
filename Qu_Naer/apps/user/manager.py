from django.contrib.auth.models import UserManager
from django.utils import timezone
from apps.profile.models import *

class CustomeUserManager(UserManager):

     def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username and is_superuser:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if is_superuser:
            UserProfile.create_user_profile(user_id=user.id,
                                            user_password=password,
                                            user_email=username,
                                            user_mobile=None,
                                            user_nick=None,
                                            register_ip=None,
                                            sex=2,
                                            province=None,
                                            city=None,
                                            district=None)
        return user

     def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

     def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)