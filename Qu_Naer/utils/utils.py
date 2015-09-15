# -*- encoding: utf-8 -*-
#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from main import settings
import re, sys
import string
import hashlib
import datetime
import random
from django.utils import timezone

REQUEST_METHOD_ERROR = 'REQUEST METHOD ERROR'
reload(sys)
sys.setdefaultencoding('utf-8')

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
    in_str = '$%^&*(±)9!@£/{}' + in_str + '$%^&*(±)9!@£/{}'
    m = hashlib.md5()
    m.update(in_str.encode('utf-8'))
    return m.hexdigest()

def random_bits(bits_length):
    """
    """
    return random.getrandbits(bits_length)

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

def html_template_wrapper(htmlfile, rep_pattern, rep_str):
    """
    """
    with open(htmlfile, 'rb') as fp:
        msg = fp.read()
        msg = string.replace(msg, rep_pattern, rep_str)
        return MIMEText(msg, 'html', 'utf-8')

def send_email(receiver, subject=None, message=None, html_str=None):
    """
    REF: https://docs.python.org/2/library/smtplib.html
    """
    sender = settings.EMAIL_SENDER

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    # msg = "[Active] Register Info from " + settings.SITE_NAME

    if subject is None:
        msg["Subject"] = "[Info] Register Info from " + settings.SITE_NAME
    else:
        msg["Subject"] = subject

    msg["From"] = sender
    msg["To"] = receiver

    content = None
    if message is not None:
        content = MIMEText(message, 'plain', 'utf-8')

    if html_str is not None:
        content = html_str

    # Send the message via local SMTP server.
    msg.attach(content)
    s = smtplib.SMTP('localhost')

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(sender, receiver, content.as_string())
    print "[INFO] Sucess Send Active Email to account: " + receiver
