from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.views import View
from accounts.models import MyUser
from accounts.forms import SetPasswordForm


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
