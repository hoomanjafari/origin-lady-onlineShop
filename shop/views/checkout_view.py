from django.shortcuts import (render, redirect)
from django.views import View
from django.contrib import messages
from accounts.models import UserAddress
from accounts.forms import UserAddressForm


# add user adress form function is in this class too (in function post)
class CheckOutView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request, 'برای ادامه مراحل پرداخت لطفا با شماره موبایل خود ثبت نام کنید در سایت',
                             'success')
            request.session['payment_url'] = 'shop:checkout'
            return redirect('accounts:register')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        user_address = UserAddress.objects.filter(user=request.user.id)
        return render(request, 'shop/checkout.html', {'user_address': user_address})

    def post(self, request):
        user_address = UserAddress.objects.filter(user=request.user.id)
        form = UserAddressForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            UserAddress.objects.create(
                user=request.user,
                name=cd['name'],
                family=cd['family'],
                address_mobile=cd['address_mobile'],
                state=cd['state'],
                city=cd['city'],
                address=cd['address'],
                postal_code=cd['postal_code']
            )
            return redirect('payment:payment')
        print(form.errors)
        messages.error(request, 'لطفا تمام اطلاعات خواسته شده را با دقت پر کنید', 'danger')
        return render(request, 'shop/checkout.html', {'user_address': user_address})
