from django.shortcuts import (render, redirect)
from django.contrib import messages
from django.views import View
from django.conf import settings
import json
import requests
from shop.models import AddCart
from payment.models import (Payment, ItemOrdered)


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"


class VerifyRequestView(View):
    def get(self, request):
        t_authority = request.GET['Authority']
        customer = AddCart.objects.filter(customer=request.user)
        phone = request.user.mobile
        amount = 0
        for person in customer:
            amount += int(person.total_price)
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            'Authority': t_authority
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        res = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if res.status_code == 200:
            response = res.json()
            cart = AddCart.objects.filter(customer=request.user)
            if response['Status'] == 100:
                payment = Payment.objects.create(
                    customer=request.user,
                    status=f"Status : {response['Status']}, موفق",
                    total_paid=f'{amount}تومان ',
                    track_id=response['RefID']
                )
                # to pass data for payment receipt
                request.session['payment_id'] = payment.id

                for i in cart:
                    ItemOrdered.objects.create(
                        customer=request.user,
                        payment=payment,
                        item=i.selected_product,
                        item_quantity=i.selected_quantity,
                        item_color=i.selected_color,
                        item_size=i.selected_size
                    )
                # to clearing the card items
                cart.delete()
                print(f"Successful -- Status : {response['Status']}, RefId : {response['RefID']}")
                messages.success(request, 'پرداخت با موفقیت انجام شد', 'success')
                return redirect('payment:payment_success')
            else:
                print(f"Failed To Pay -- Status : {response['Status']}, Ref_id : {response['RefID']}")
                messages.error(request, 'پرداخت با شکست مواجه شد', 'danger')
                return redirect('payment:payment_failed')

        return res.json()
