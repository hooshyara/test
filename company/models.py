from django.db import models


class MainCompany(models.Model):
    COMPANY = [
        ('شرکت حمل و نقل بین المللی بارجامه توس', 'شرکت حمل و نقل بین المللی بارجامه توس'),
        ('شرکت حمل و نقل بین المللی فردوس راه', 'شرکت حمل و نقل بین المللی فردوس راه'),
        ('شرکت حمل و نقل بین المللی سلمان ترابر توس', 'شرکت حمل و نقل بین المللی سلمان ترابر توس'),
        ("شرکت حمل و نقل بین المللی مشاهیر شرق", "شرکت حمل و نقل بین المللی مشاهیر شرق"),
        ('بار متفرقه مجموعه سلمان ترابر', 'بار متفرقه مجموعه سلمان ترابر'),
        ("all", "all")
        
    ]
    main_company = models.CharField(max_length=200, choices=COMPANY, null=True, blank=True)

    def __str__(self):
        return self.main_company
class Company(models.Model):
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    commission = models.IntegerField(default=0)
    commission_intermediary = models.IntegerField(default=0) # کمیسون واسطه
    bill_insurance = models.IntegerField(default=0) #بیمه راهنامه 
    code = models.PositiveIntegerField(null=True, blank=True)

