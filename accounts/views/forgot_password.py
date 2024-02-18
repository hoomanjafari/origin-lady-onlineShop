from django.shortcuts import (render, redirect)
from django.contrib import messages
from django.views import View
from accounts.models import MyUser
from accounts.forms import ForgotPasswordForm
from accounts import my_otp_ghasedak


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'accounts/forgot_password.html')

    def post(self, request):
        form = ForgotPasswordForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = MyUser.objects.filter(mobile=cd['forgot_mobile'], is_active=True)
            if user.exists():
                otp = my_otp_ghasedak.otp_random()
                expiration_time_left = my_otp_ghasedak.time_left(cd['forgot_mobile'])
                if not my_otp_ghasedak.check_expiration(cd['forgot_mobile']):
                    user = MyUser.objects.get(mobile=cd['forgot_mobile'])
                    user.otp = otp
                    user.save()
                    request.session['forgot_password_mobile'] = cd['forgot_mobile']
                    print(otp)
                    return redirect('accounts:forgot_password_verify')
                elif my_otp_ghasedak.check_expiration(cd['forgot_mobile']):
                    messages.error(request, f'برای ارسال مجدد باید کد قبلی منضی شود ({expiration_time_left}'
                                            f' ثانیه باقیمانده)', 'danger')
                    return redirect('accounts:forgot_password')
            else:
                messages.error(request, 'این شماره قبلا داخل این سایت ثبت نام نکرده است', 'danger')
                print('mona2')
                return redirect('accounts:forgot_password')
        print(form.errors, 'mona3')
        return render(request, 'accounts/forgot_password.html')
