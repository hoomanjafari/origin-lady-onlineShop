from django.contrib import admin
from .models import (Payment, ItemOrdered)


admin.site.register(Payment)
admin.site.register(ItemOrdered)
