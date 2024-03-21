from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.views import View
from django.contrib.auth import login
from accounts.models import MyUser
from shop.models import AddCart
from accounts.forms import SetPasswordForm


class SetPasswordView(View):

    def dispatch(self, request, *args, **kwargs):
        requested_user = request.session.get('user_mobile')
        if not requested_user:
            return redirect('accounts:register')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'accounts/set_password.html')

    def post(self, request):
        form = SetPasswordForm(self.request.POST)
        requested_user = request.session.get('user_mobile')
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(MyUser, mobile=requested_user)
            user.set_password(cd['password'])
            user.save()
            guest_cart = AddCart.objects.filter(guest_session_id=request.session.session_key)
            if guest_cart:
                for item in guest_cart:
                    item.customer = user
                    item.guest_session_id = None
                    item.save()
                login(request, user)
                del request.session['user_mobile']
                messages.success(request, 'ثبت نام با موفقیت انجام شد و حالا در حساب خود هستین ', 'success')
                payment_url = request.session.get('payment_url')
                if payment_url is not None:
                    del request.session['payment_url']
                    return redirect(payment_url)
                return redirect('index:go_home')
            elif not guest_cart:
                del request.session['user_mobile']
                messages.success(request, 'ثبت نام با موفقیت انجام شد'
                                          ' و حالا از بخش ورود میتوانید وارد حساب خود شوید', 'success')
                return redirect('index:go_home')
        messages.error(request, 'رمز عبور و تکرار رمز عبور یکسان نیستند', 'danger')
        return render(request, 'accounts/set_password.html')
