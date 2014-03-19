import hashlib
import rsa
from functools import wraps
from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils.http import urlquote
from django.http import HttpResponseForbidden
from django.conf import settings
from django.utils.decorators import available_attrs
# from main.settings import ACCESS_KEY

def user_authenticate(test_func):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.FILES:
                pass
            print(request.user)
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            #if settings.DEBUG:
            #    return view_func(request, *args, **kwargs)
            return dict(code=1002, msg="Access Deny! AnonymousUser")
        return _wrapped_view
    return decorator


def ajax_login_required(function=None):
    """
    Decorator for views that checks that the user is logged in, return
    access deny if the user is not logged in.
    """
    actual_decorator = user_authenticate(
        lambda u: u.is_authenticated()
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# def signature_required(function=None):
#     """
#     Decorator for verify requests is originated by legal client, return
#     access deny if the request lacks a a.
#     md5(ACCESS_KEY + parameter-string +ACCESS_KEY)
#     """
#     def decorator(view_function):
#         @wraps(view_function, assigned=available_attrs(view_function))
#         def _wrapper(request, *args, **kwargs):
#             print(request.META['HTTP_SIGNATURE'])
#             if request.META['HTTP_SIGNATURE']:
#                 key_list = sorted(list(dict(request.POST).keys()))
#                 print(key_list)
#                 s = ''.join(key_list)
#                 m = hashlib.md5()
#                 m.update(ACCESS_KEY.encode(encoding='utf8'))
#                 m.update(s.encode(encoding='utf8'))
#                 m.update(ACCESS_KEY.encode(encoding='utf8'))
#                 a = m.hexdigest()
#                 print(a)
#                 if request.META['HTTP_SIGNATURE'] == a:
#                     return view_function(request, *args, **kwargs)
#                 else:
#                     return dict(code=1001, msg="Access Deny! (reason: wrong signature)")
#             return dict(code=1000, msg="Access Deny! (reason: signature does not exist)")
#         return _wrapper
#     return decorator(function)


def admin_only(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if not request.user.is_staff:
                return HttpResponseForbidden()
            else:
                return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)

def get_user(request):
    if not hasattr(request, 'user'):
        user = request
    else:
        user = request.user

    if user.is_anonymous():
        user = cache.get('user:%s' % settings.HOMEPAGE_USERNAME, None)
        if not user:
            try:
                user = User.objects.get(username=settings.HOMEPAGE_USERNAME)
                cache.set('user:%s' % user, user)
            except User.DoesNotExist:
                user = User.objects.create(username=settings.HOMEPAGE_USERNAME)
                user.set_password('')
                user.save()
    return user

def invalidate_template_cache(fragment_name, *variables):
    args = hashlib.md5(u':'.join([urlquote(var) for var in variables]))
    cache_key = 'template.cache.%s.%s' % (fragment_name, args.hexdigest())
    cache.delete(cache_key)

def generate_secret_token(phrase, size=12):
    """Generate a (SHA1) security hash from the provided info."""
    info = (phrase, settings.SECRET_KEY)
    return hashlib.sha1("".join(info)).hexdigest()[:size]

def cryptography_decorator(func):
    """
    Decorator for preprocessing data of encryption and decryption.
    """
    def wrap(info):
        try:
            if isinstance(info, str):
                info = info.encode()
            elif isinstance(info, bytes):   None
            else:   raise TypeError
            return func(info)
        except TypeError:
            print("TypeError in %s: input argument type %s, but expected type %s" % (func.__name__, type(info), type(b'')))
        except OverflowError:
            print("%s bytes needs for message, but there is only space for 373" % len(info))
        except Exception as e:
            print(e)
    return wrap

@cryptography_decorator
def generate_secret_hash_3072_sha1(info):
    """
    Generate a (SHA1) security hash (3072bits) from the provide info.
    url - http://stuvel.eu/files/python-rsa-doc/usage.html
    Input:
        - info: this should be in binary format
    """
    return rsa.encrypt(info, settings.PUB_KEY)

@cryptography_decorator
def decrypted_hash_3072_sha1(encrpted_info):
    """
    Decrpted a (SHA1) security hash from the provide encrpyted info.
    url - http://stuvel.eu/files/python-rsa-doc/usage.html
    Input:
        - encrypted_info: the encrypted info message from clients
    """
    try:
        return rsa.decrypt(encrpted_info, settings.PRI_KEY)
    except:
        # Need more work
        print("DecryptionError! If someone change the encrypted message from user, this exception may raise!")

def extract_user_agent(request):
    user_agent = request.environ.get('HTTP_USER_AGENT', '').lower()
    platform = '------'
    if 'ipad app' in user_agent:
        platform = 'iPad'
    elif 'iphone app' in user_agent:
        platform = 'iPhone'
    elif 'blar' in user_agent:
        platform = 'Blar'
    elif 'android' in user_agent:
        platform = 'Androd'
    elif 'pluggio' in user_agent:
        platform = 'Plugio'
    elif 'msie' in user_agent:
        platform = 'IE'
        if 'msie 9' in user_agent:
            platform += '9'
        elif 'msie 10' in user_agent:
            platform += '10'
        elif 'msie 8' in user_agent:
            platform += '8'
    elif 'chrome' in user_agent:
        platform = 'Chrome'
    elif 'safari' in user_agent:
        platform = 'Safari'
    elif 'meego' in user_agent:
        platform = 'MeeGo'
    elif 'firefox' in user_agent:
        platform = 'FF'
    elif 'opera' in user_agent:
        platform = 'Opera'
    elif 'wp7' in user_agent:
        platform = 'WP7'
    elif 'wp8' in user_agent:
        platform = 'WP8'
    elif 'tafiti' in user_agent:
        platform = 'Tafiti'
    elif 'readkit' in user_agent:
        platform = 'ReadKt'
    elif 'metroblur' in user_agent:
        platform = 'Metrob'
    elif 'feedme' in user_agent:
        platform = 'FeedMe'
    elif 'feed reader-window' in user_agent:
        platform = 'FeedRe'
    elif 'feed reader-background' in user_agent:
        platform = 'FeReBg'

    return platform
