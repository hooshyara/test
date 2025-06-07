from rest_framework import serializers
from .models import *

class TariffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'

class WarehousingTariffSerializers(serializers.ModelSerializer):
    class Meta:
        model = WarehousingTariff
        fields = '__all__'