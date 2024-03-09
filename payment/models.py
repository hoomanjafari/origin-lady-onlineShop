from django.db import models
from accounts.models import MyUser
from shop.models import (AddCart, AllClothes)


class Payment(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=33)
    total_paid = models.CharField(max_length=33)
    paid_time = models.DateTimeField(auto_now_add=True)
    track_id = models.CharField(max_length=33)

    def __str__(self):
        return f'( {self.customer} ) -- ( {self.status} ) -- ( {self.total_paid}) -- (id: {self.id})'


class ItemOrdered(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='item_ordered_customer')
    # this payment null n blank shall be remove
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='item_ordered_payment',
                                null=True, blank=True)
    item = models.ForeignKey(AllClothes, on_delete=models.CASCADE, related_name='item_ordered_product')
    item_quantity = models.CharField(max_length=10)
    item_color = models.CharField(max_length=33, null=True, blank=True)
    item_size = models.CharField(max_length=33, null=True, blank=True)
    # this paid time null n blank shall be removed
    paid_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'({self.customer}) - (payment_Id : {self.payment.id}) - ({self.item.item_name} x{self.item_quantity})'
