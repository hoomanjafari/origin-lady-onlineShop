from django.shortcuts import (render, redirect)
from django.contrib import messages
from django.views import View
from accounts.models import MyUser
from accounts.forms import VerifyFrom
from accounts import my_otp_ghasedak


class VerifyView(View):

    def dispatch(self, request, *args, **kwargs):
        requested_user = request.session.get('user_mobile')
        if not requested_user:
            return redirect('accounts:register')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        mobile = request.session.get('user_mobile')
        return render(request, 'accounts/verify.html', {'mobile': mobile})

    def post(self, request):
        form = VerifyFrom(self.request.POST)
        mobile = request.session.get('user_mobile')
        if form.is_valid():
            cd = form.cleaned_data
            mobile_otp = MyUser.objects.get(mobile=mobile)
            cd_otp = cd['otp_1'] + cd['otp_2'] + cd['otp_3'] + cd['otp_4']
            if int(mobile_otp.otp) == int(cd_otp) and my_otp_ghasedak.check_expiration(mobile):
                mobile_otp.is_active = True
                mobile_otp.save()
                # messages.success(request, 'ثیت نام انجام شد'
                return redirect('accounts:set_password')
            elif int(mobile_otp.otp) != int(cd_otp) and my_otp_ghasedak.check_expiration(mobile):
                messages.error(request, 'کد وارد شده صحیح نیست دوباره تلاش کنید', 'danger')
                return redirect('accounts:verify')

            elif not my_otp_ghasedak.check_expiration(mobile):
                del request.session['user_mobile']
                messages.error(request, 'کد وارد شده منقضی شده است ... مجدد درخواست کد جدید کنید', 'danger')
                return redirect('accounts:register')
        return render(request, 'accounts/verify.html', {'mobile': mobile})
