from django.shortcuts import render
from django.views import View
from shop.models import AllClothes


class ShopTshirtView(View):
    def get(self, request):
        tshirt = AllClothes.objects.all().filter(item_category=3)
        return render(request, 'shop/shop_tshirt.html', {'tshirt': tshirt})


class ShopBeachShirtView(View):
    def get(self, request):
        beach_shirt = AllClothes.objects.all().filter(item_category=1)
        return render(request, 'shop/shop_beach_shirt.html', {'beach_shirt': beach_shirt})


class ShopUnderWearView(View):
    def get(self, request):
        under_wear = AllClothes.objects.all().filter(item_category=4)
        return render(request, 'shop/shop_under_wear.html', {'under_wear': under_wear})


class ShopHatsView(View):
    def get(self, request):
        hats = AllClothes.objects.all().filter(item_category=7)
        return render(request, 'shop/shop_hats.html', {'hats': hats})


class ShopLegsView(View):
    def get(self, request):
        legs = AllClothes.objects.all().filter(item_category=5)
        return render(request, 'shop/shop_legs.html', {'legs': legs})


class ShopShomizView(View):
    def get(self, request):
        shomiz = AllClothes.objects.all().filter(item_category=2)
        return render(request, 'shop/shop_shoomiz.html', {'shomiz': shomiz})


class ShopTopsView(View):
    def get(self, request):
        tops = AllClothes.objects.all().filter(item_category=6)
        return render(request, 'shop/shop_tops.html', {'tops': tops})
