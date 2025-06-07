from django.db import models
from company.models import MainCompany
from booking.models import Sailing
class Tariff(models.Model):
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING)
    sailing = models.ForeignKey(Sailing, on_delete=models.DO_NOTHING) #کشنیرانی
    payment_method = models.ForeignKey(Sailing, on_delete=models.DO_NOTHING, null=False, related_name='payment_method') #نوع پرداخت
    until_day = models.PositiveBigIntegerField(null=True)
    from_day = models.PositiveBigIntegerField(null=True)
    foot = models.PositiveBigIntegerField(null=True)
    sailing_price = models.PositiveIntegerField(null=True) # بهای کشتیرانی
    code = models.PositiveIntegerField(null=True, blank=True)
    # parent = models.CharField(max_length=100, null=True, blank=True)

class WarehousingTariff(models.Model): #تعرفه انبار داری
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING)
    max_days = models.PositiveBigIntegerField() #حداکثر روز
    foot = models.PositiveBigIntegerField() #فوت
    price = models.PositiveIntegerField(null=True) #مبلغ
    code = models.PositiveIntegerField(null=True, blank=True)
    # parent = models.CharField(max_length=100, null=True, blank=True)