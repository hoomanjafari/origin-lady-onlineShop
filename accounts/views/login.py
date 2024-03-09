from django.shortcuts import (render, redirect)
from django.contrib.auth import (login, authenticate, logout)
from django.contrib import messages
from django.views import View
from accounts.forms import LoginForm
from shop.models import AddCart


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
            guest_cart = AddCart.objects.filter(guest_session_id=request.session.session_key)
            payment_url = request.session.get('payment_url')
            if user is not None:
                login(request, user)
                # to save geust cart in his account cart
                if guest_cart is not None:
                    for i in guest_cart:
                        i.customer = user
                        i.save()
                # to redirect user to checkout page
                if payment_url is not None:
                    messages.success(request, 'وارد حساب کاریری خود شدید', 'success')
                    del request.session['payment_url']
                    return redirect(payment_url)

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
        messages.success(request, 'شما از حساب خود با موفقیت خارج شدید', 'success')
        return redirect('accounts:login')
