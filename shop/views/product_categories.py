from django.shortcuts import render
from django.views import View
from shop.models import AllClothes


class ShopTshirtView(View):
    def get(self, request):
        tshirt = AllClothes.objects.all().filter(item_category=3)
        default = 'ترتیب نمایش'
        if request.GET.get('selected'):
            tshirt = AllClothes.objects.filter(item_category=3).order_by(request.GET['selected'])
            default = request.GET.get('selected')
            if default == '-added_time':
                default = 'جدید ترین ها'
            elif default == 'added_time':
                default = 'قدیمی ترین ها'
            elif default == 'item_price':
                default = 'ارزان ترین ها'
            elif default == '-item_price':
                default = 'گران ترین ها'
            elif default == 'discount':
                default = 'تخفیف خورده ها'
                tshirt = AllClothes.objects.filter(item_category=3, discount=True)
        return render(request, 'shop/shop_tshirt.html', {
            'tshirt': tshirt, 'default': default
        })


class ShopBeachShirtView(View):
    def get(self, request):
        beach_shirt = AllClothes.objects.all().filter(item_category=1)
        default = 'ترتیب نمایش'
        if request.GET.get('selected'):
            beach_shirt = AllClothes.objects.filter(item_category=1).order_by(request.GET['selected'])
            default = request.GET.get('selected')
            if default == '-added_time':
                default = 'جدید ترین ها'
            elif default == 'added_time':
                default = 'قدیمی ترین ها'
            elif default == 'item_price':
                default = 'ارزان ترین ها'
            elif default == '-item_price':
                default = 'گران ترین ها'
            elif default == 'discount':
                default = 'تخفیف خورده ها'
                beach_shirt = AllClothes.objects.filter(item_category=1, discount=True)
        return render(request, 'shop/shop_beach_shirt.html', {'beach_shirt': beach_shirt, 'default': default})


class ShopUnderWearView(View):
    def get(self, request):
        under_wear = AllClothes.objects.all().filter(item_category=4)
        default = 'ترتیب نمایش'
        if request.GET.get('selected'):
            under_wear = AllClothes.objects.filter(item_category=4).order_by(request.GET['selected'])
            default = request.GET.get('selected')
            if default == '-added_time':
                default = 'جدید ترین ها'
            elif default == 'added_time':
                default = 'قدیمی ترین ها'
            elif default == 'item_price':
                default = 'ارزان ترین ها'
            elif default == '-item_price':
                default = 'گران ترین ها'
            elif default == 'discount':
                default = 'تخفیف خورده ها'
                under_wear = AllClothes.objects.filter(item_category=4, discount=True)
        return render(request, 'shop/shop_under_wear.html', {'under_wear': under_wear, 'default': default})


class ShopHatsView(View):
    def get(self, request):
        hats = AllClothes.objects.all().filter(item_category=7)
        default = 'ترتیب نمایش'
        if request.GET.get('selected'):
            hats = AllClothes.objects.filter(item_category=7).order_by(request.GET['selected'])
            default = request.GET.get('selected')
            if default == '-added_time':
                default = 'جدید ترین ها'
            elif default == 'added_time':
                default = 'قدیمی ترین ها'
            elif default == 'item_price':
                default = 'ارزان ترین ها'
            elif default == '-item_price':
                default = 'گران ترین ها'
            elif default == 'discount':
                default = 'تخفیف خورده ها'
                hats = AllClothes.objects.filter(item_category=7, discount=True)
        return render(request, 'shop/shop_hats.html', {'hats': hats, 'default': default})


class ShopLegsView(View):
    def get(self, request):
        legs = AllClothes.objects.all().filter(item_category=5)
        default = 'ترتیب نمایش'
        if request.GET.get('selected'):
            legs = AllClothes.objects.filter(item_category=5).order_by(request.GET['selected'])
            default = request.GET.get('selected')
            if default == '-added_time':
                default = 'جدید ترین ها'
            elif default == 'added_time':
                default = 'قدیمی ترین ها'
            elif default == 'item_price':
                default = 'ارزان ترین ها'
            elif default == '-item_price':
                default = 'گران ترین ها'
            elif default == 'discount':
                default = 'تخفیف خورده ها'
                legs = AllClothes.objects.filter(item_category=5, discount=True)
        return render(request, 'shop/shop_legs.html', {'legs': legs, 'default': default})


class ShopShomizView(View):
    def get(self, request):
        shomiz = AllClothes.objects.all().filter(item_category=2)
        default = 'ترتیب نمایش'
        if request.GET.get('selected'):
            shomiz = AllClothes.objects.filter(item_category=2).order_by(request.GET['selected'])
            default = request.GET.get('selected')
            if default == '-added_time':
                default = 'جدید ترین ها'
            elif default == 'added_time':
                default = 'قدیمی ترین ها'
            elif default == 'item_price':
                default = 'ارزان ترین ها'
            elif default == '-item_price':
                default = 'گران ترین ها'
            elif default == 'discount':
                default = 'تخفیف خورده ها'
                shomiz = AllClothes.objects.filter(item_category=2, discount=True)
        return render(request, 'shop/shop_shoomiz.html', {'shomiz': shomiz, 'default': default})


class ShopTopsView(View):
    def get(self, request):
        tops = AllClothes.objects.all().filter(item_category=6)
        default = 'ترتیب نمایش'
        if request.GET.get('selected'):
            tops = AllClothes.objects.filter(item_category=6).order_by(request.GET['selected'])
            default = request.GET.get('selected')
            if default == '-added_time':
                default = 'جدید ترین ها'
            elif default == 'added_time':
                default = 'قدیمی ترین ها'
            elif default == 'item_price':
                default = 'ارزان ترین ها'
            elif default == '-item_price':
                default = 'گران ترین ها'
            elif default == 'discount':
                default = 'تخفیف خورده ها'
                tops = AllClothes.objects.filter(item_category=6, discount=True)
        return render(request, 'shop/shop_tops.html', {'tops': tops, 'default': default})
