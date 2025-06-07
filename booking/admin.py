from django.contrib import admin
from .models import *

@admin.register(Sailing)
class SailingAdmin(admin.ModelAdmin):
    model = Sailing
    fields = ['title', 'name',]

    list_display = ['id', 'title']

@admin.register(OwnersOfGoods)
class OwnersOfGoodsAdmin(admin.ModelAdmin):
    model = OwnersOfGoods
    fields = ['name', 'tel', 'mobile', 'fax', 'address', 'commission',]

@admin.register(BillDescribtion)
class BillDescribtionAdmin(admin.ModelAdmin):
    model = BillDescribtion
    fields = ['get_documents_type', 'bill_lading_number', 'ship',
               'Owners_of_goods', 'Free_Time', 'demurrage_type', 
               'containers_count', 'total_weight_load', 'perweight', 
               'total_product_count', 'per_product_count', 'Reference_code', 
               'ship_name', 'sub_date', 'active', "company"]
    
    readonly_fields = ['sub_date']

@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    model = Trailer
    fields = ['title', 'name',]

@admin.register(TruckType)
class TruckTypeAdmin(admin.ModelAdmin):
    model = TruckType
    fields = ['title', 'name',]

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    model = Truck
    fields = ['truck_type', 'country', 'License_plate_number', 
              'Smart_cart_number', 'Transit_number', 'trailer', 
              'address', 'insurance_number', 'license_number', 
              'Hood_number', 'date_issuance_hood', 'date_validity_hood', 
              'owner_name', 'mobile', 'Annual_contract_number']

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    model = Carrier
    fields = ['title', 'name',]



@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    model = Route
    fields = ['source_country', 'source_city', 'distinction_country', 
              'distinction_city', 'Insuranceـpremium', 'Driver_exemption', 
              'Price_per_ton_kilometer', 'Container_departure_price', 'title']

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    model = Station
    fields = ['route', 'name']



@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    model = Driver
    fields = ['name', 'country', 'national_id', 'tel', 'mobile', 
              'smart_cart_number', 'cart_number', 'cart_validate', 
              'Booklet_number', 'Certificate_number', 'Certificate_validate', 
              'address']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    fields = ['booking_number', 'continer_number', 'loading_date', 
              'guide_num', 'product_weight', 'carrier', 'route', 
              'truck', 'owners_of_goods', 'rent', 'tonnageـweight', 
              'tonnageـamount', 'commission_type', 'commission_percent', 
              'commission_amount', 'total_amount_owners_of_goods', 
              'company_info', 'driver', 'placedـnumber', 'rent_driver', 
              'tonnage_count_driver', 'tonnageـamount_driver', 'portـcommission', 
              'parking', 'perrent_port', 'total_amount_driver', 
              'driver_accountـbalance', 'difference', 'discribtion', 'guide', 
              'company']
    list_display = ['id', 'guide', 'booking_number']

@admin.register(DeliveryRecipientCMR)
class DeliveryRecipientCMRAdmin(admin.ModelAdmin):
    model = DeliveryRecipientCMR
    fields = ['title', 'name']

@admin.register(DeliveryRecipientProduct)
class DeliveryRecipientProductAdmin(admin.ModelAdmin):
    model = DeliveryRecipientProduct
    fields = ['title', 'name', ]

@admin.register(DeliveryRecipientBill)
class DeliveryRecipientBillAdmin(admin.ModelAdmin):
    model = DeliveryRecipientBill
    fields = ['title', 'name', ]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    fields = ['title', 'name']

@admin.register(Country)
class CityAdmin(admin.ModelAdmin):
    model = Country
    fields = ['title', 'name']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = ['title', 'name']

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    model = Insurance
    fields = ['title', 'name']

@admin.register(PackagingType)
class PackagingTypeAdmin(admin.ModelAdmin):
    model = PackagingType
    fields = ['title', 'name']

@admin.register(GetDocumentType)
class GetDocumentTypeAdmin(admin.ModelAdmin):
    model = GetDocumentType
    fields = ['title', 'name']
    list_display = ['id']

@admin.register(EnterType)
class EnterTypeAdmin(admin.ModelAdmin):
    model = EnterType
    fields = ['title', 'name']
 
@admin.register(PostalCompany)
class PostalCompanyAdmin(admin.ModelAdmin):
    model = PostalCompany
    fields = ['title', 'name']

@admin.register(CostList)
class CostListAdmin(admin.ModelAdmin):
    model = CostList
    fields = ['title', 'name']

@admin.register(DemurrageType)
class DemurrageTypeAdmin(admin.ModelAdmin):
    model = DemurrageType
    fields = ['title', 'name',]

@admin.register(CmrBarjame)
class CmrBarjameAdmin(admin.ModelAdmin):
    model = CmrBarjame
    fields = ['title', 'name']

@admin.register(CmrFerdows)
class CmrFerdowsAdmin(admin.ModelAdmin):
    model = CmrFerdows
    fields = ['title', 'name']

@admin.register(CmrMashahir)
class CmrMashahirAdmin(admin.ModelAdmin):
    model = CmrMashahir
    fields = ['title', 'name']

@admin.register(CmrSalamn)
class CmrSalamnAdmin(admin.ModelAdmin):
    model = CmrSalamn
    fields = ['title', 'name']


@admin.register(Continer)
class ContinerAdmin(admin.ModelAdmin):
    model = Continer
    fields = ['number', 'invoice', 'size', 'Date_receipt_documents', 'product',
               'product_count', 'packet_type', 'carrier', 'national_id',
                'download_date', 'status', 'warehouse_receipt_date', 
                'weight_documents', 'weight_bascol', 'difference_weight', 
                'excess_tonnage', 'serial_number', 'route', 'truck', 
                'commission', 'fare_amount', 'advance_rent_amount', 'driver', 
                'contract_number', 'freeTime', 'description', 'bill', ]
    
    list_display = ["file_number",'bill', 'serial_number', 'contract_number']
    

@admin.register(Demurrage)
class DemurrageAdmin(admin.ModelAdmin):
    model = Demurrage
    fields = ['continer' ,'demurrage_typpe', 'type_info', 'date',
            'price', 'description', 'file', 'company']
    
@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    model = Guide
    fields = ['continer' ,'guide_number', 'guide_id_salman',
               'guide_id_ferdows', 'guide_id_barjame',
                'guide_id_mashahir', 'sender', 'receiver','carrier', 
                'next_carrier','carrier_descriptions', 'place_date_delivery_goods',
                'location_date_loading','attached_documents', 'sign_number', 
                'download_info', 'pure_agreements','sender_instructions' , 
                'place_date_issue', 'date_place_receipt_goods', 'company', 
                'is_active', 'confirm_date', 'is_valid']
    
    readonly_fields = ['confirm_date']
    list_display = ['id', 'continer', 'is_valid', 'guide_number']

@admin.register(VolumeGuide)
class VolumeGuideAdmin(admin.ModelAdmin):
    model = VolumeGuide
    fields = ['guide' ,'descriptions', 'volume',]

@admin.register(ExitContiner)
class ExitContinerAdmin(admin.ModelAdmin):
    model = ExitContiner
    fields = ['continer' ,'exit_date', 'types',]

@admin.register(MiscellaneousLoad)
class MiscellaneousLoadAdmin(admin.ModelAdmin):
    model = MiscellaneousLoad
    fields = ['continer' ,'main_company', 'des_company']

@admin.register(LoadingFees)
class LoadingFeesAdmin(admin.ModelAdmin):
    model = LoadingFees
    fields = ['continer' ,'company', 'cost', 'date', 'description', 'fees']

    list_display = ['id', 'continer']

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    model = Log
    fields = ['booking' ,'status', 'company', 'update_status', 'update_date']
    list_display = ['id', 'booking', 'status']
    readonly_fields = ['update_date']

@admin.register(SumFees)
class SumFeesAdmin(admin.ModelAdmin):
    model = Log
    fields = ['continer' , 'sum_fees']
    list_display = ['id', 'continer', 'sum_fees']
  
