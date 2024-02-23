from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.views import View
from .models import (AllClothes, AddCart,)
from accounts.models import MyUser
from .forms import AddCartForm


class ShopTshirtView(View):
    def get(self, request):
        tshirt = AllClothes.objects.all().filter(item_category='3')
        return render(request, 'shop/shop_tshirt.html', {'tshirt': tshirt})

    def post(self, request):
        pass


class ProductDetails(View):
    def get(self, request, **kwargs):
        product = get_object_or_404(AllClothes, pk=kwargs['pk'])
        colores = product.available_colores.all()
        url_data = product.main_image.url
        sizes = product.available_sizes.all()

        return render(request, 'shop/product-details.html', {
            'product': product, 'colores': colores, 'url_data': url_data, 'sizes': sizes,
        })

    def post(self, request, **kwargs):
        form = AddCartForm(self.request.POST)
        product = get_object_or_404(AllClothes, pk=kwargs['pk'])
        colores = product.available_colores.all()
        url_data = product.main_image.url
        sizes = product.available_sizes.all()

        if form.is_valid():
            cd = form.cleaned_data
            if request.user.is_authenticated:
                user = get_object_or_404(MyUser, pk=request.user.id)
                already_exists = AddCart.objects.filter(customer=user, selected_product=product)
                if not already_exists.exists():
                    AddCart.objects.create(
                        customer=user,
                        selected_product=product,
                        selected_color=cd['selected_color'],
                        selected_size=cd['selected_size'],
                        selected_quantity=cd['selected_quantity'],
                        total_price=cd['total_price'],
                    )
                    messages.success(request, 'این محصول با موفقیت به سبد خرید شما اضافه شد', 'success')
                    return redirect('shop:product_details', pk=product.id)
                else:
                    messages.error(request, 'این محصول درحال حاضر در سبد خرید شما وجود دارد', 'danger')
                    return redirect('shop:product_details', pk=product.id)
            else:
                guest_user = request.session.session_key
                already_exists = AddCart.objects.filter(guest_session_id=guest_user, selected_product=product)
                if not already_exists.exists():
                    AddCart.objects.create(
                        guest_session_id=guest_user,
                        selected_product=product,
                        selected_color=cd['selected_color'],
                        selected_size=cd['selected_size'],
                        selected_quantity=cd['selected_quantity'],
                        total_price=cd['total_price'],
                    )
                    messages.success(request, 'این محصول با موفقیت به سبد خرید شما اضافه شد', 'success')
                    return redirect('shop:product_details', pk=product.id)
                else:
                    messages.error(request, 'این محصول درحال حاضر در سبد خرید شما وجود دارد', 'danger')
                    return redirect('shop:product_details', pk=product.id)
        print(form.errors)
        messages.error(request, 'لطفا رنگ و سایز مورد نظرتون رو انخاب کنبد (با کلیک کردن بر روی ان ها)', 'danger')
        return render(request, 'shop/product-details.html', {
            'product': product, 'colores': colores, 'url_data': url_data, 'sizes': sizes, 'form': form,
        })

