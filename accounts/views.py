from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .models import MyUser, UserAddress
from .forms import (
    RegisterForm, VerifyFrom, SetPasswordForm, LoginForm, ProfileEditForm, UserAddressForm, ForgotPasswordForm
)
from . import my_otp_ghasedak


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
            del request.session['user_mobile']
            messages.success(request, 'ثبت نام با موفقیت انجام شد ', 'success')
            return redirect('index:go_home')
        messages.error(request, 'رمز عبور و تکرار رمز عبور یکسان نیستند', 'danger')
        return render(request, 'accounts/set_password.html')


class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index:go_home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(mobile=cd['mobile'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'وارد حساب کاریری خود شدید', 'success')
                return redirect('index:go_home')
            messages.error(request,
                           'شماره موبایل یا رمز عبور اشتباه هست (اگر رمز ورود خود را فراموش کردین از فراموشی رمز عبور استفاده کنید) '
                           , 'danger'
                           )
            return redirect('accounts:login')
        return render(request, 'accounts/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index:go_home')


class ProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, pk=kwargs['pk'])
        user_address = UserAddress.objects.filter(user=user)
        return render(request, 'accounts/profile.html', {'user': user, 'user_address': user_address})

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, pk=kwargs['pk'])
        form = ProfileEditForm(self.request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'تعغیرات اعمال شدن', 'success')
            return redirect('accounts:profile', pk=user.id)
        return render(request, 'accounts/profile.html', {'form': form})


class UserAddressView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        else:
            return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, pk=request.user.id)
        form = UserAddressForm(self.request.POST, instance=user)
        if form.is_valid():
            cd = form.cleaned_data
            UserAddress.objects.create(
                user=user,
                name=cd['name'],
                family=cd['family'],
                address_mobile=cd['address_mobile'],
                state=cd['state'],
                city=cd['city'],
                address=cd['address'],
                postal_code=cd['postal_code']
            )
            messages.success(request, 'ادرس ذخیره شد', 'success')
            return redirect('accounts:profile', pk=user.id)
        else:
            messages.error(request, 'اطلاعات وارد شده صحیح نیست لطفا با دقت بیشتر اطلاعات رو وارد کنید', 'danger')
            print(form.errors)
            return redirect('accounts:profile', pk=user.id)


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
                    messages.error(request, f'برای ارسال مجدد باید کد قبلی منضی شود ({expiration_time_left} ثانیه باقیمانده)', 'danger')
                    return redirect('accounts:forgot_password')
            else:
                messages.error(request, 'این شماره قبلا داخل این سایت ثبت نام نکرده است', 'danger')
                print('mona2')
                return redirect('accounts:forgot_password')
        print(form.errors, 'mona3')
        return render(request, 'accounts/forgot_password.html')


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


class SetNewPasswordView(View):
    def dispatch(self, request, *args, **kwargs):
        forgot_password_mobile = request.session.get('forgot_password_mobile')
        if not forgot_password_mobile:
            return redirect('accounts:forgot_password')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'accounts/set_new_password.html')

    def post(self, request):
        form = SetPasswordForm(self.request.POST)
        forgot_password_mobile = request.session.get('forgot_password_mobile')
        user = get_object_or_404(MyUser, mobile=forgot_password_mobile)
        if form.is_valid():
            cd = form.cleaned_data
            user.set_password(cd['password'])
            user.save()
            messages.success(request, 'تغییر رمز ورود به حساب کاربری با موفقیت انجام شد', 'success')
            del request.session['forgot_password_mobile']
            return redirect('index:go_home')
        messages.error(request, 'رمز عبور و تکرار رمز عبور یکسان نیستند', 'danger')
        return redirect('accounts:set_new_password')
