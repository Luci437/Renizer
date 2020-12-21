from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LoginInfo)
admin.site.register(HairStyles)
admin.site.register(Booking)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Billing)
admin.site.register(BillingItem)
admin.site.register(BillingCard)
admin.site.register(BillingAddress)