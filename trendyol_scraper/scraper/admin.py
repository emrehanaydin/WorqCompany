from django.contrib import admin
from .models import Product
from .models import Merchant


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("product_name", "price")
    list_display = ("product_name", "price", "brand", "category")


class MerchantAdmin(admin.ModelAdmin):
    search_fields = ("merchant_name", "score")
    list_display = ("merchant_name", "score")


admin.site.register(Product, ProductAdmin)
admin.site.register(Merchant, MerchantAdmin)
