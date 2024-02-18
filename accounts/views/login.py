from django.shortcuts import (render, redirect)
from django.contrib.auth import (login, authenticate, logout)
from django.contrib import messages
from django.views import View
from accounts.forms import LoginForm


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
                           'شماره موبایل یا رمز عبور اشتباه هست'
                           ' (اگر رمز ورود خود را فراموش کردین از فراموشی رمز عبور استفاده کنید) '
                           , 'danger'
                           )
            return redirect('accounts:login')
        return render(request, 'accounts/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index:go_home')