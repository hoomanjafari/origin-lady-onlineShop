from django.shortcuts import (render, redirect)
from django.views import View
from payment.models import Payment


class PaymentSuccessView(View):

    def dispatch(self, request, *args, **kwargs):
        payment_access = request.session.get('payment_access')
        if payment_access is None:
            return redirect('index:go_home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        payment = Payment.objects.get(id=request.session.get('payment_id'))
        del request.session['payment_id']
        del request.session['payment_access']
        return render(request, 'payment/payment_success.html', {'payment': payment})


class PaymentFailedView(View):

    def dispatch(self, request, *args, **kwargs):
        payment_access = request.session.get('payment_access')
        if payment_access is None:
            return redirect('index:go_home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        del request.session['payment_access']
        return render(request, 'payment/payment_error.html')
