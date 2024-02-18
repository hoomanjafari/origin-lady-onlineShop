from django.shortcuts import (render, redirect)
from django.contrib import messages
from django.views import View
from accounts.models import MyUser
from accounts.forms import RegisterForm
from accounts import my_otp_ghasedak


class RegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index:go_home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'accounts/register.html', )

    def post(self, request):
        form = RegisterForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = MyUser.objects.get(mobile=cd['mobile'])
                expiration_time_left = my_otp_ghasedak.time_left(user.mobile)
                if not my_otp_ghasedak.check_expiration(cd['mobile']) and user.is_active is False:
                    otp = my_otp_ghasedak.otp_random()
                    user.otp = otp
                    user.save()
                    messages.success(request, 'کد ارسال شد', 'success')
                    request.session['user_mobile'] = cd['mobile']
                    # request.session['user_otp'] = otp # it was needed for passing this value to js
                    print('otp is :', otp)
                    return redirect('accounts:verify')
                elif my_otp_ghasedak.check_expiration(cd['mobile']) and user.is_active is False:
                    messages.error(request, f'برای ارسال مجدد باید کد قبلی منضی شود ({expiration_time_left} ثانیه باقیمانده)', 'danger')
                    return redirect('accounts:register')
                elif user.is_active is True:
                    messages.error(request, 'شما قبلا ثبت نام کردین اگر رمز ورود خود را فراموش کردین از ( فراموشی رمز عبور ) استفاده کنید', 'danger')
                    return redirect('accounts:login')
            except MyUser.DoesNotExist:
                otp = my_otp_ghasedak.otp_random()
                MyUser.objects.create_user(mobile=cd['mobile'], is_active=False, otp=otp)
                request.session['user_mobile'] = cd['mobile']
                # request.session['user_otp'] = otp # it was needed for passing this value to js
                messages.success(request, 'کد ارسال شد', 'success')
                print('otp is :', otp)
                return redirect('accounts:verify')

        return render(request, 'accounts/register.html')