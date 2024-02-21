from django.db import models


class Colores(models.Model):
    color = models.CharField(max_length=22)

    def __str__(self):
        return f'{self.color}'


class Sizes(models.Model):
    size = models.CharField(max_length=22)

    def __str__(self):
        return f'{self.size}'


class Tshirt(models.Model):
    available_colores = models.ManyToManyField(Colores,)
    available_sizes = models.ManyToManyField(Sizes,)
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
        return f'{self.item_info[:30]} ... --- {self.item_name}'
