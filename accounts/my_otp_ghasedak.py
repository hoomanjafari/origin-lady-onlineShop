from ghasedakpack import *
import random
import datetime
from .models import MyUser


def otp_ghasedak(mobile, otp):
    mobile = [mobile, ]

    sms = ghasedakpack.Ghasedak("362633836c992b3fca7e2294253b508e93dec48468f89917f3fd3a9636612928")
    sms.verification({
        'receptor': mobile, 'type': '1', 'template': "origin6bazar", 'param1': '',
    })

    print(mobile, otp)


def otp_random():
    return random.randint(1000, 9999)


def check_expiration(mobile):
    try:
        user = MyUser.objects.get(mobile=mobile)
        now = datetime.datetime.now()
        otp_time = user.otp_created_time
        deff_time = now - otp_time

        if deff_time.seconds > 120:
            return False
        return True
    except MyUser.DoesNotExist:
        return False


def time_left(mobile):
    try:
        user = MyUser.objects.get(mobile=mobile)
        now = datetime.datetime.now()
        otp_time = user.otp_created_time
        dif_time = now - otp_time

        return 120 - dif_time.seconds
    except MyUser.DoesNotExist:
        return False