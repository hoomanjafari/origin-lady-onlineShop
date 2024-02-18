from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.views import View
from accounts.models import MyUser
from accounts.forms import VerifyFrom
from accounts import my_otp_ghasedak


class ForgotPasswordVerifyView(View):
    def dispatch(self, request, *args, **kwargs):
        forgot_password_mobile = request.session.get('forgot_password_mobile')
        if not forgot_password_mobile:
            return redirect('accounts:forgot_password')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        mobile = request.session.get('forgot_password_mobile')
        return render(request, 'accounts/forgot_password_verify.html', {'forgot_password_mobile': mobile})

    def post(self, request):
        form = VerifyFrom(self.request.POST)
        forgot_password_mobile = request.session.get('forgot_password_mobile')
        user = get_object_or_404(MyUser, mobile=forgot_password_mobile)
        if form.is_valid():
            cd = form.cleaned_data
            cd_otp = cd['otp_1'] + cd['otp_2'] + cd['otp_3'] + cd['otp_4']
            if int(user.otp) == int(cd_otp) and my_otp_ghasedak.check_expiration(forgot_password_mobile):
                return redirect('accounts:set_new_password')
            elif not my_otp_ghasedak.check_expiration(forgot_password_mobile):
                del request.session['forgot_password_mobile']
                messages.error(request, 'کد وارد شده منقضی شده است ... مجدد درخواست کد جدید کنید', 'danger')
                return redirect('accounts:forgot_password')
            elif int(user.otp) != int(cd_otp) and my_otp_ghasedak.check_expiration(forgot_password_mobile):
                messages.error(request, 'کد وارد شده صحیح نیست دوباره تلاش کنید', 'danger')
                return redirect('accounts:forgot_password_verify')
        return redirect('accounts:forgot_password_verify')
