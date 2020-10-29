from django.contrib import admin

from .models import *

class OrderItemDisplay(admin.ModelAdmin):

    list_display = ('product','order','quantity')

class Ooc(admin.ModelAdmin):
    list_display = ('customer',)


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem,OrderItemDisplay)
admin.site.register(ShippingAddress)
