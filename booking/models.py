from django.db import models
from company.models import Company, MainCompany




class Sailing(models.Model): # کشتیرانی
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class OwnersOfGoods(models.Model): # صاحبان کالا
    name = models.CharField(max_length=100) #اسم
    tel = models.CharField(max_length=100, null=True) #تلفن ثابت
    mobile = models.CharField(max_length=100, null=True) #تلفن همراه
    fax = models.CharField(max_length=100, null=True) #فکس
    address = models.TextField(null=True)
    commission = models.PositiveBigIntegerField(default=0, null=True) #کمیسیون
    code = models.PositiveIntegerField(null=True, blank=True)

class GetDocumentType(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name



class DemurrageType(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)

class BillDescribtion(models.Model): # مشخصات بارنامه
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING, null=True, blank=True)
    get_documents_type = models.ForeignKey(GetDocumentType, on_delete=models.SET_NULL, null=True) #روش دریافت مدرک
    bill_lading_number = models.CharField(max_length=100) #شماره بارنامه
    active = models.BooleanField(default=True, null=True)
    ship = models.ForeignKey(Sailing, on_delete=models.SET_NULL, null=True) #نام کشتیرانی
    Owners_of_goods = models.ForeignKey(OwnersOfGoods, on_delete=models.SET_NULL, null=True) #نام صاحب کالا
    Free_Time = models.PositiveIntegerField(null=True, blank=True) #مهلت مجاز
    sub_date = models.DateField(auto_now_add=True, null=True)
    demurrage_type = models.ForeignKey(DemurrageType, on_delete=models.SET_NULL, null=True) #نوع دموراژ
    containers_count = models.IntegerField() #تعداد کانتینر
    total_weight_load = models.PositiveIntegerField() #وزن کل بار
    perweight = models.IntegerField(null=True) #وزن باقیمانده
    total_product_count = models.IntegerField() #تعداد کل کالا
    per_product_count = models.IntegerField(null=True) #کالاهای باقی مانده
    Reference_code = models.CharField(max_length=100, null=True) #کد مرجع
    ship_name = models.CharField(max_length=100, null=True) #نام کشتی
    code = models.PositiveIntegerField(null=True, blank=True)
class Trailer(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class TruckType(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class Country(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class Truck(models.Model):
    truck_type = models.ForeignKey(TruckType, on_delete=models.SET_NULL, null=True) #مدل کامیون
    country = models.ForeignKey(Country, on_delete=models.SET_NULL ,null=True) #کشور
    License_plate_number = models.CharField(max_length=100) #شماره پلاک
    Smart_cart_number = models.CharField(max_length=100, null=True) #شماره کارت هوشمند
    Transit_number = models.CharField(max_length=100, null=True) #شماره ترانزیت
    trailer = models.ForeignKey(Trailer, on_delete=models.SET_NULL, null=True) #نوع تریلر
    address = models.TextField(null=True) #آدرس
    insurance_number = models.CharField(max_length=100, null=True) #شماره بیمه
    license_number = models.CharField(max_length=100, null=True) #شماره پروانه
    Hood_number = models.CharField(max_length=100, null=True) #شماره کاپوتاژ
    date_issuance_hood = models.DateField(null=True, blank=True) #تاریخ صدور کاپوتاژ
    date_validity_hood = models.DateField(null=True, blank=True) #تاریخ اعتبار کاپوتاژ
    owner_name = models.CharField(max_length=100, null=True) #نام و نام خانوادگی مالک
    mobile = models.CharField(max_length=13, null=True) #تلفن همراه
    Annual_contract_number = models.CharField(max_length=100, null=True) #شماره قرارداد سالیانه
    code = models.PositiveIntegerField(null=True, blank=True)
class Carrier(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)

class Route(models.Model):
    title = models.CharField(max_length=100, null=True)
    source_country = models.CharField(max_length=100) #کشور مبدا
    source_city = models.CharField(max_length=100) #شهر مبدا
    distinction_country = models.CharField(max_length=100) #کشور مقصد
    distinction_city = models.CharField(max_length=100, null=True, blank=True) #شهر مقصد
    Insuranceـpremium = models.PositiveBigIntegerField(null=True, blank=True) #حق بیمه
    Driver_exemption = models.PositiveBigIntegerField(null=True, blank=True) #معافیت راننده
    Price_per_ton_kilometer = models.PositiveBigIntegerField(null=True, blank=True) #بهای تن کیلومتر
    Container_departure_price = models.PositiveBigIntegerField(null=True, blank=True) #بهای خروج کانتینر
    code = models.PositiveIntegerField(null=True, blank=True)
class Station(models.Model): # ایستگاه
    name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)

class Driver(models.Model):
    name = models.CharField(max_length=100) #نام و نام خانوادگی
    country = models.CharField(max_length=100, null=True) #کشور
    national_id = models.CharField(max_length=100, null=True) #کدملی / شماره پاسپورت
    tel = models.CharField(max_length=100, null=True) #تلفن ثابت
    mobile = models.CharField(max_length=100, null=True) #تلفن همراه
    smart_cart_number = models.CharField(max_length=100, null=True) #شماره کارت هوشمند
    cart_number = models.CharField(max_length=100, null=True) #شماره کارت
    cart_validate = models.DateField(null=True) #تاریخ اعتبار کارت
    Booklet_number = models.CharField(max_length=100, null=True) #شماره دقترچه
    Booklet_validate = models.DateField(null=True) #تاریخ اعتبار دقترچه
    Certificate_number = models.CharField(max_length=100, null=True) #شماره گواهینامه
    Certificate_validate = models.DateField(null=True) #تاریخ اعتبار گواهینامه
    address = models.CharField(max_length=100, null=True) #آدرس
    code = models.PositiveIntegerField(null=True, blank=True)

class Booking(models.Model):
    COMMISSION_TYPE = [
        ('کرایه', 'کرایه'),
        ('فاقد کمیسیون', 'فاقد کمیسیون'),
        ('کرایه و اضافه تناژ', 'کرایه و اضافه تناژ'),
    ]
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING ,null=True, blank=True)
    booking_number = models.PositiveBigIntegerField(null=True) #شماره بوکینگ
    guide = models.ForeignKey("Guide", on_delete=models.SET_NULL, null=True, unique=True) #راهنامه
    continer_number = models.ForeignKey("Continer", null=True, on_delete=models.DO_NOTHING) #شماره کانتینر
    loading_date = models.DateField(null=True) #تاریح بارگیری
    guide_num = models.CharField(max_length=100, null=True) #شماره راهنامه
    product_weight = models.PositiveIntegerField(null=True) #وزن کالا
    carrier = models.ForeignKey(Carrier, on_delete=models.SET_NULL, null=True) #شرکت حمل کننده
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True) #مسیر
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True) #کامیون
    owners_of_goods = models.ForeignKey(OwnersOfGoods, on_delete=models.SET_NULL, null=True) #صاحب کالا
    rent = models.PositiveBigIntegerField(default=0, null=True) #کرایه
    tonnageـweight = models.PositiveBigIntegerField(default=0, null=True) #وزن اضافه تناژ
    tonnage_count = models.PositiveBigIntegerField(default=0, null=True) #مقدار اضافه تناژ
    tonnageـamount = models.PositiveBigIntegerField(default=0, null=True) #مبلغ اضافه تناژ
    commission_type = models.CharField(max_length=100, choices=COMMISSION_TYPE, null=True) #نوع کمیسیون
    commission_percent = models.PositiveIntegerField(null=True) #درصد کمیسیون
    commission_amount = models.PositiveBigIntegerField(null=True) #مبلغ کمیسیون
    total_amount_owners_of_goods = models.PositiveBigIntegerField(default=0, null=True) #جمع کل حساب صاحب کالا
    company_info = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True) #اطلاعات شرکت
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True) #راننده
    # bill = models.ForeignKey(BillDescribtion, null=True, blank=True, on_delete=models.DO_NOTHING)
    placedـnumber = models.PositiveBigIntegerField(null=True) #شماره قرارداد
    rent_driver = models.PositiveBigIntegerField(default=0, null=True) #کرایه 
    tonnage_count_driver = models.PositiveBigIntegerField(default=0, null=True) #مقدار اضافه تناژ
    tonnageـamount_driver = models.PositiveBigIntegerField(default=0, null=True) #مبلغ اضافه تناژ
    portـcommission = models.PositiveBigIntegerField(null=True) #کمیسیون بندر
    parking = models.PositiveBigIntegerField(default=0, null=True) #پارکینگ
    perrent_port = models.PositiveBigIntegerField(null=True) #پیش کرایه بندر
    total_amount_driver = models.PositiveBigIntegerField(null=True) #جمع کل راننده
    driver_accountـbalance = models.PositiveBigIntegerField(null=True) #مانده حساب راننده
    difference = models.PositiveBigIntegerField(null=True) #مابه تفاوت
    discribtion = models.TextField(null=True) #توضیحات

class DeliveryRecipientCMR(models.Model): #تحویل گیرنده CMR 
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class DeliveryRecipientProduct(models.Model): #تحویل گیرنده کالا 
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class DeliveryRecipientBill(models.Model): #تحویل گیرنده بارنامه 
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class City(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class Product(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class Insurance(models.Model): #بیمه
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class PackagingType(models.Model): # نوع بسته بندی
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)

class EnterType(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class CostList(models.Model): #  لیست بها
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)   
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class CmrSalamn(models.Model): # راهنامه سلمان 
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)  
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class CmrBarjame(models.Model): # راهنامه بارجامه    
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)  
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class CmrFerdows(models.Model): # راهنامه قردوس  
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)  
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class CmrMashahir(models.Model): # راهنامه مشاهیر   
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)  
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class PostalCompany(models.Model): # شرکت پست   
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)  
    code = models.PositiveIntegerField(null=True, blank=True)
    parent = models.CharField(max_length=100, null=True, blank=True)
class Continer(models.Model):
    # booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING, null=True, related_name='booking')
    number = models.CharField(max_length=100)
    file_number = models.AutoField(primary_key=True)
    invoice = models.CharField(max_length=100,null=True, blank=True) #صورتحساب
    size = models.PositiveBigIntegerField()
    Date_receipt_documents = models.DateField()
    bill = models.ForeignKey(BillDescribtion, on_delete=models.DO_NOTHING, null=True,)
    product = models.ForeignKey(Product, null=True, on_delete=models.DO_NOTHING)
    product_count = models.CharField(max_length=100, null=True, blank=True)
    packet_type = models.ForeignKey(PackagingType, null=True, on_delete=models.DO_NOTHING)
    carrier = models.ForeignKey(Carrier, on_delete=models.DO_NOTHING, null=True)
    national_id = models.CharField(max_length=100, null=True)
    download_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True)
    warehouse_receipt_date = models.DateField(null=True, blank=True)
    weight_documents = models.PositiveBigIntegerField(null=True)
    weight_bascol = models.PositiveBigIntegerField(null=True, default=0)
    difference_weight = models.PositiveBigIntegerField(null=True)
    excess_tonnage = models.PositiveBigIntegerField(null=True, default=0)
    serial_number = models.PositiveBigIntegerField(null=True, default=0)
    route = models.ForeignKey(Route, on_delete=models.DO_NOTHING, null=True)
    truck = models.ForeignKey(Truck, on_delete=models.DO_NOTHING, null=True)
    commission = models.PositiveBigIntegerField(null=True)
    fare_amount = models.PositiveBigIntegerField(null=True, default=0) # مبلغ کرایه
    advance_rent_amount = models.PositiveBigIntegerField(null=True, default=0) #مبلغ پیش کرایه
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, null=True)
    contract_number = models.PositiveBigIntegerField(null=True, default=0) #شماره قرارداد
    freeTime = models.PositiveBigIntegerField(null=True, default=0)
    description = models.TextField(null=True, blank=True)

class Guide(models.Model):
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING ,null=True, blank=True)
    continer = models.ForeignKey(Continer, on_delete=models.DO_NOTHING, null=True, unique=True)
    guide_number = models.PositiveBigIntegerField(null=True, blank=True)
    guide_id_salman = models.ForeignKey(CmrSalamn ,null=True, blank=True, on_delete=models.DO_NOTHING)
    guide_id_ferdows = models.ForeignKey(CmrFerdows ,null=True, blank=True, on_delete=models.DO_NOTHING)
    guide_id_barjame = models.ForeignKey(CmrBarjame ,null=True, blank=True, on_delete=models.DO_NOTHING)
    guide_id_mashahir = models.ForeignKey(CmrMashahir ,null=True, blank=True, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    sender = models.TextField(null=True, blank=True)
    receiver = models.TextField(null=True, blank=True)
    carrier = models.TextField(null=True, blank=True) #حمل کننده
    next_carrier = models.TextField(null=True, blank=True) #حمل کننده بعدی
    carrier_descriptions = models.TextField(null=True, blank=True) #توضیحات و ملاحضات حمل کننده
    place_date_delivery_goods = models.TextField(null=True, blank=True) # . محل و تاریخ تحویل کالا
    location_date_loading = models.TextField(null=True, blank=True) # محل و تاریخ بارگیری
    attached_documents = models.TextField(null=True, blank=True) #اسناد ضمیمه
    sign_number =models.TextField(null=True, blank=True) # علامت و شماره
    download_info = models.TextField(null=True, blank=True)
    pure_agreements =models.TextField(null=True, blank=True) # توافق های خالص
    sender_instructions =models.TextField(null=True, blank=True) #دستورات فرستنده
    place_date_issue = models.TextField(null=True, blank=True) # محل و تاریخ صدور
    date_place_receipt_goods = models.TextField(null=True, blank=True) #تاریخ و محل دریافت کالا
    confirm_date = models.DateField(auto_now_add=True, null=True, blank=True) # تاریخ ثبت
    is_valid = models.BooleanField(default=False, null=True)
    
class VolumeGuide(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.DO_NOTHING , null=True)
    descriptions = models.TextField(null=True, blank=True) # وزن خالص توضیحات
    volume = models.PositiveBigIntegerField() #حجم



class Demurrage(models.Model):
    TYPE = [
        ('دموراژ', 'دموراژ'),
        ('خسارت', 'خسارت'),
    ]
    DEMURRAGE_TYPE = [
        ('راننده', 'راننده'),
        ('صاحب کالا', 'صاحب کالا'),
        ('کشتیرانی', 'کشتیرانی')
    ]
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING , null=True, blank=True)
    continer = models.ForeignKey(Continer, on_delete=models.DO_NOTHING, null=True)
    demurrage_typpe = models.CharField(choices=DEMURRAGE_TYPE, max_length=100, null=True, blank=True)
    type_info = models.CharField(choices=TYPE, max_length=100)
    date = models.DateField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    dem_file = models.FileField(upload_to='file/%Y/%m/%d/', null=True)

class ExitContiner(models.Model):
    TYPE = [
        ('کانتینرهای خارج شده', 'کانتینرهای خارج شده'),
        ('کانتینرهای خارج نشده', 'کانتینرهای خارج نشده'),
        ('کانتینرهای مهلت خروج گذشته', 'کانتینرهای مهلت خروج گذشته'),
    ]
    # company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING)
    continer = models.ForeignKey(Continer, on_delete=models.CASCADE, null=True)
    exit_date = models.DateField(null=True, blank=True)
    types = models.CharField(max_length=100, choices=TYPE, null=True, default='کانتینرهای خارج نشده')
    code = models.PositiveIntegerField(null=True, blank=True)

class MiscellaneousLoad(models.Model): # بار متفرقه
    continer = models.ForeignKey(Continer, on_delete=models.DO_NOTHING)
    main_company = models.ForeignKey(MainCompany, null=True, on_delete=models.DO_NOTHING)
    des_company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING, related_name='des_company', null=True)

class LoadingFees(models.Model): # هزینه های بارگیری
    continer = models.ForeignKey(Continer, on_delete=models.DO_NOTHING, null=True)
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING, null=True, blank=True)
    cost = models.ForeignKey(CostList, on_delete=models.DO_NOTHING, null=True)
    date = models.DateField(null=True)
    fees = models.PositiveBigIntegerField(default=0, null=True)
    description = models.TextField(null=True)
    code = models.PositiveIntegerField(null=True, blank=True)

class Log(models.Model):
    STATUS = [
        ('دیده شده', 'دیده شده'),
        ('دیده نشده', 'دیده نشده'),
    ]
    company = models.ForeignKey(MainCompany, on_delete=models.DO_NOTHING,null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default='دیده نشده')
    update_status = models.BooleanField(default=False)
    COMMISSION_TYPE = [
        ('کرایه', 'کرایه'),
        ('فاقد کمیسیون', 'فاقد کمیسیون'),
        ('کرایه و اضافه تناژ', 'کرایه و اضافه تناژ'),
    ]
    # booking_number = models.CharField(max_length=100, null=True) #شماره بوکینگ
    guide = models.ForeignKey("Guide", on_delete=models.SET_NULL, null=True) #راهنامه
    continer_number = models.ForeignKey("Continer", null=True, on_delete=models.DO_NOTHING) #شماره کانتینر
    loading_date = models.DateField(null=True) #تاریح بارگیری
    guide_num = models.CharField(max_length=100, null=True) #شماره راهنامه
    product_weight = models.PositiveIntegerField(null=True) #وزن کالا
    carrier = models.ForeignKey(Carrier, on_delete=models.SET_NULL, null=True) #شرکت حمل کننده
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True) #مسیر
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True) #کامیون
    owners_of_goods = models.ForeignKey(OwnersOfGoods, on_delete=models.SET_NULL, null=True) #صاحب کالا
    rent = models.PositiveBigIntegerField(default=0, null=True) #کرایه
    tonnageـweight = models.PositiveBigIntegerField(default=0, null=True) #وزن اضافه تناژ
    tonnage_count = models.PositiveBigIntegerField(default=0, null=True) #مقدار اضافه تناژ
    tonnageـamount = models.PositiveBigIntegerField(default=0, null=True) #مبلغ اضافه تناژ
    commission_type = models.CharField(max_length=100, choices=COMMISSION_TYPE, null=True) #نوع کمیسیون
    commission_percent = models.PositiveIntegerField(null=True) #درصد کمیسیون
    commission_amount = models.PositiveBigIntegerField(null=True) #مبلغ کمیسیون
    total_amount_owners_of_goods = models.PositiveBigIntegerField(default=0, null=True) #جمع کل حساب صاحب کالا
    company_info = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True) #اطلاعات شرکت
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True) #راننده
    # bill = models.ForeignKey(BillDescribtion, null=True, blank=True, on_delete=models.DO_NOTHING)
    placedـnumber = models.PositiveBigIntegerField(null=True) #شماره قرارداد
    rent_driver = models.PositiveBigIntegerField(default=0, null=True) #کرایه 
    tonnage_count_driver = models.PositiveBigIntegerField(default=0, null=True) #مقدار اضافه تناژ
    tonnageـamount_driver = models.PositiveBigIntegerField(default=0, null=True) #مبلغ اضافه تناژ
    portـcommission = models.PositiveBigIntegerField(null=True) #کمیسیون بندر
    parking = models.PositiveBigIntegerField(default=0, null=True) #پارکینگ
    perrent_port = models.PositiveBigIntegerField(null=True) #پیش کرایه بندر
    total_amount_driver = models.PositiveBigIntegerField(null=True) #جمع کل راننده
    driver_accountـbalance = models.PositiveBigIntegerField(null=True) #مانده حساب راننده
    difference = models.PositiveBigIntegerField(null=True) #مابه تفاوت
    discribtion = models.TextField(null=True) #توضیحات
    update_date = models.DateTimeField(auto_now=True, null=True)


class SumFees(models.Model):
    continer = models.ForeignKey(Continer, on_delete=models.CASCADE, unique=True)
    sum_fees = models.PositiveBigIntegerField(default=0)