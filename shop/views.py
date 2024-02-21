from django.shortcuts import render
from django.views import View
from .models import(Tshirt)


class ShopTshirtView(View):
    def get(self, request):
        tshirt = Tshirt.objects.all()
        return render(request, 'shop/shop_tshirt.html', {'tshirt': tshirt})

    def post(self, request):
        pass


class ProductDetails(View):
    def get(self, request, **kwargs):
        product = Tshirt.objects.get(pk=kwargs['pk'])
        colores = product.available_colores.all()
        url_data = product.main_image.url
        sizes = product.available_sizes.all()
        return render(request, 'shop/product-details.html', {
            'product': product, 'colores': colores, 'url_data': url_data, 'sizes': sizes,
        })

    def post(self, request, **kwargs):
        pass
