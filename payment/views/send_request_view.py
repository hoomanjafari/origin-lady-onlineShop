from django.shortcuts import redirect
from django.views import View
from django.conf import settings
from django.contrib import messages
import json
import requests
from django.http import HttpResponse
from shop.models import AddCart


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
currency = 'IRT'
# CallbackURL should be change to real url
CallbackURL = 'http://192.168.1.6:8000/payment/pay/verify/'


class SendRequestView(View):
    def get(self, request):
        customer = AddCart.objects.filter(customer=request.user)
        phone = request.user.mobile
        amount = 0
        for person in customer:
            amount += int(person.total_price)
        print('phone is ', phone)
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Description": description,
            'metadata': {
              'mobile': phone,
            },
            "CallbackURL": CallbackURL,
            "currency": currency,
        }

        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        res = requests.post(ZP_API_REQUEST, data=data, headers=headers)

        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                # to make a session for dispatching payment urls
                request.session['payment_access'] = True
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
            else:
                print('status :', response['Status'])
                messages.error(request, 'سبد خرید شما خالی است. میتوانید از فروشگاه سایت محصول خود را انتخاب کنید', 'danger')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            e_code = res.json()['errors']['code']
            e_message = res.json()['errors']['message']
            print(f'error code : {e_code}, error message : {e_message}')
            messages.error(request, f' مشکلی در ایجاد اتصال با درگاه به وجود امده{res.status_code}', 'danger')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
