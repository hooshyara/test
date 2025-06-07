from django.contrib import admin
from .models import Tariff, WarehousingTariff

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    model = Tariff
    fields = ['sailing', 'payment_method', 'from_day', 'until_day', 'foot', 
              'sailing_price', 'company']

@admin.register(WarehousingTariff)
class WarhousingTariffAdmin(admin.ModelAdmin):
    model = WarehousingTariff
    fields = ['max_days', 'foot', 'price', 'company']
