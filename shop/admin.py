from django.contrib import admin
from .models import (Sizes, Colores, AllClothes, AddCart, ClothesCategory)


admin.site.register(Sizes)
admin.site.register(Colores)
admin.site.register(AllClothes)
admin.site.register(AddCart)
admin.site.register(ClothesCategory)
