import re
import hashlib
import datetime
from django.utils import timezone

REQUEST_METHOD_ERROR = 'REQUEST METHOD ERROR'

def is_email(email=None):
    if email is None:
        return False
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
        return True
    return False

def is_mobile_phone(mobile_phone=None):
    try:
        if mobile_phone is None:
            return False
        if re.match("^(13[0-9]|15[0|3|6|7|8|9]|18[0-9])\d{8}$", mobile_phone) is not None:
            return True
    except Exception:
        return False
    return False

def md5(in_str):
    in_str = '$%^&*(±)9!@£/<>' + in_str + '$%^&*(±)9!@£/<>'
    m = hashlib.md5()
    m.update(in_str.encode('utf-8'))
    return m.hexdigest()

def response_fail_to_mobile(code, msg):
    return dict(code=code, msg=msg)

def response_success_to_mobile(msg):
    return dict(code=1, content=msg)

def string_to_datetime(in_str):
    if in_str is None:
        return None
    return datetime.datetime.strptime(in_str, '%Y-%m-%d %H:%M:%S')

def datetime_to_string(in_date):
    if in_date is None:
        return None
    return in_date.strftime('%Y-%m-%d %H:%M:%S')

def datetime_convert_current_timezone(in_date):
    if in_date is None:
        return None
    return in_date.astimezone(timezone.get_current_timezone())
