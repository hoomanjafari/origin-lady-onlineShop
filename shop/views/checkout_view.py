from django.shortcuts import (render, redirect, get_object_or_404)
from django.views import View
from django.contrib import messages
from accounts.models import UserAddress
from shop.models import AddCart
from accounts.forms import UserAddressForm
from shop.forms import EditItemCartForm
from django.http import JsonResponse


# add user adress form function is in this class too (in function post)
# Edit Cart Item class is in this file too

class CheckOutView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request, 'برای ادامه مراحل پرداخت لطفا با شماره موبایل خود ثبت نام کنید در سایت',
                             'success')
            request.session['payment_url'] = 'shop:checkout'
            return redirect('accounts:register')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        user_address = UserAddress.objects.filter(user=request.user.id)
        return render(request, 'shop/checkout.html', {'user_address': user_address, })

    def post(self, request):
        user_address = UserAddress.objects.filter(user=request.user.id)
        form = UserAddressForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            UserAddress.objects.create(
                user=request.user,
                name=cd['name'],
                family=cd['family'],
                address_mobile=cd['address_mobile'],
                state=cd['state'],
                city=cd['city'],
                address=cd['address'],
                postal_code=cd['postal_code']
            )
            return redirect('payment:payment')
        print(form.errors)
        messages.error(request, 'لطفا تمام اطلاعات خواسته شده را با دقت پر کنید', 'danger')
        return render(request, 'shop/checkout.html', {'user_address': user_address})


class EditItemCartView(View):
    def post(self, request):
        try:
            product_id = request.session.get('edited_item_id')
            print('productId is =', product_id)
            edit_item = AddCart.objects.get(pk=product_id)
            form = EditItemCartForm(self.request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if cd['edit_size'] == '' and cd['edit_quantity'] != '':
                    edit_item.selected_quantity = cd['edit_quantity']
                    edit_item.total_price = int(cd['edit_quantity']) * int(edit_item.selected_product.item_price)
                    edit_item.save()
                elif cd['edit_quantity'] == '' and cd['edit_size'] != '':
                    edit_item.selected_size = cd['edit_size']
                    edit_item.save()
                elif cd['edit_size'] == '' and cd['edit_quantity'] == '':
                    del request.session['edited_item_id']
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                else:
                    edit_item.selected_size = cd['edit_size']
                    edit_item.selected_quantity = cd['edit_quantity']
                    edit_item.total_price = int(cd['edit_quantity']) * int(edit_item.selected_product.item_price)
                    edit_item.save()
                messages.success(request, 'تغیرات ذخیره شد', 'success')
                del request.session['edited_item_id']
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            else:
                messages.error(request, 'somthing went wrong', 'danger')
                print('errors : ', form.errors)
                del request.session['edited_item_id']
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        except AddCart.DoesNotExist:
            product_id = request.session.get('edited_item_id')
            print('product id :', product_id, 'does not exists')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def get_edited_item_id(request):
    request.session['edited_item_id'] = request.POST.get('product_id')
    edited_item_id = request.session.get('edited_item_id')
    response = JsonResponse({'AllRight': edited_item_id})
    return response
