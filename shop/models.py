from django.db import models
from accounts.models import MyUser


class Colores(models.Model):
    color = models.CharField(max_length=22)

    def __str__(self):
        return f'{self.color}'


class Sizes(models.Model):
    size = models.CharField(max_length=22)

    def __str__(self):
        return f'{self.size}'


class ClothesCategory(models.Model):
    category = models.CharField(max_length=33)

    def __str__(self):
        return f'{self.category} --- id : {self.id}'


class AllClothes(models.Model):
    available_colores = models.ManyToManyField(Colores,)
    available_sizes = models.ManyToManyField(Sizes,)
    item_category = models.ForeignKey(ClothesCategory, on_delete=models.CASCADE, related_name='allClothes_itemCategory')
    item_name = models.CharField(max_length=33)
    item_info = models.TextField()
    item_price = models.PositiveIntegerField()
    added_time = models.DateTimeField(auto_now_add=True)

    main_image = models.ImageField(upload_to='img/%y%m%d%H%M')
    image_white = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)
    image_orange = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)
    image_pink = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)
    image_purple = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)
    image_blue = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)
    image_red = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)
    image_black = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)
    image_green = models.ImageField(upload_to='img/%y%m%d%H%M', blank=True, null=True)

    def __str__(self):
        return f'(info : { self.item_info[:30]}... ) --- (name : {self.item_name} ) ' \
               f'-- (category : {self.item_category} id: {self.item_category.id})'


class AddCart(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='addCart_customer')
    selected_product = models.ForeignKey(AllClothes, on_delete=models.CASCADE, related_name='addCart_selectedProduct')
    selected_color = models.CharField(max_length=22)
    selected_size = models.CharField(max_length=22)
    selected_quantity = models.CharField(max_length=4)
    total_price = models.CharField(max_length=9)
    order_time = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.selected_product}) -- ( customer_number : ' \
               f' {self.customer} ) -- ( total price {self.total_price} )'