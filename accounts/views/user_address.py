from django.shortcuts import (get_object_or_404, redirect)
from django.contrib import messages
from django.views import View
from accounts.models import (MyUser, UserAddress)
from accounts.forms import UserAddressForm


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


class RemoveAddressView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        address = UserAddress.objects.get(pk=kwargs['pk'])
        address.delete()
        messages.error(request, 'ادرس با موفقیت حذف شد', 'success')
        return redirect('accounts:profile', pk=request.user.id)
