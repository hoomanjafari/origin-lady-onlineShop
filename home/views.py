from django.shortcuts import render
from django.views import View
from shop.models import AllClothes


class GoHome(View):
    def get(self, request):
        discounted_clothes = AllClothes.objects.filter(discount=True)
        new_products = AllClothes.objects.all().order_by('-added_time')
        return render(request, 'index/index.html', {
            'discounted_clothes': discounted_clothes, 'new_products': new_products
        })
