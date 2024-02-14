from random import randint
from kavenegar import *


def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI('3039676D435872564E776454664E66515764504F2F307457313747714D46554743714951796B4747366E383D')
        params = {
            'sender': '',  # optional
            'receptor': mobile,  # multiple mobile number, split by comma
            'message': 'Your otp is {}'.format(otp),
        }
        response = api.sms_send(params)
        print('otp', otp)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000, 9999)
