from rest_framework import serializers
from .models import *

class SailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sailing
        fields = '__all__'
class OwnersOfGoodsSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = OwnersOfGoods
        fields = ['id', 'name', 'tel', 'mobile', 
                  'fax', 'address', 'commission']
        
class BillDescribtionSeriallizer(serializers.ModelSerializer):
    get_documents_type_name = serializers.CharField(source='get_documents_type.name', read_only=True)
    company_name = serializers.CharField(source='company.main_company', read_only=True)
    Owners_of_goods_name = serializers.CharField(source='Owners_of_goods.name', read_only=True)
    ship_name = serializers.CharField(source='ship.name', read_only=True)
    demurrage_type_name = serializers.CharField(source='demurrage_type_.name', read_only=True)

    class Meta:
        model = BillDescribtion
        fields = ['id', 'company_name', 'get_documents_type_name', 'bill_lading_number', 
                  'ship_name', 'Owners_of_goods_name', 'Free_Time', 
                  'demurrage_type_name','containers_count','total_weight_load', 
                  'perweight','total_product_count', 'per_product_count', 
                  'Reference_code','ship_name' ]
        
class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class StationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class InsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class TruckSerializers(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class CarrierSerializers(serializers.ModelSerializer):

    class Meta:
        model = Carrier
        fields = '__all__'

class TruckTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TruckType
        fields = '__all__'

class TrailerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = '__all__'

class PackagingTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PackagingType
        fields = '__all__'

class DeliveryRecipientCMRSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRecipientCMR
        fields = '__all__'

class DeliveryRecipientProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRecipientProduct
        fields = '__all__'


class DeliveryRecipientBillSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRecipientBill
        fields = '__all__'

class Cityserializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class Countryserializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'      

class BookingSerializers(serializers.ModelSerializer):
    # company_name = serializers.CharField(source='company.main_company', read_only=True)
    # company_info_name = serializers.CharField(source='company_info.name', read_only=True)
    owners_of_goods_name = serializers.CharField(source='owners_of_goods.name', read_only=True)
    # guide_name = serializers.CharField(source='guide.guide_number', read_only=True)
    # carrier_name = serializers.CharField(source='carrier.name', read_only=True)
    # route_name = serializers.CharField(source='route.source_city', read_only=True)
    # truck_name = serializers.CharField(source='truck.License_plate_number', read_only=True)
    # continer_number_name = serializers.CharField(source='continer_number.number', read_only=True)
    # driver_name = serializers.CharField(source='driver.name', read_only=True)

    class Meta:
        model = Booking
        fields = ['id','company','booking_number','guide','continer_number','loading_date', 
                  'guide_num','product_weight','carrier','route','truck','owners_of_goods_name', 
                  'rent','tonnageـweight','tonnage_count','tonnageـamount','commission_type', 
                  'commission_percent','commission_amount','total_amount_owners_of_goods', 
                  'company_info','driver','placedـnumber','rent_driver','tonnage_count_driver', 
                  'tonnageـamount_driver','portـcommission','parking','perrent_port', 
                  'total_amount_driver','driver_accountـbalance','difference','discribtion',]

class GetDocumentTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = GetDocumentType
        fields = ["id" , 'title', 'name']

class PostalCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = PostalCompany
        fields = '__all__'


class CostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CostList
        fields = '__all__'

class EnterTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = EnterType
        fields = '__all__'

class DemurrageTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = DemurrageType
        fields = '__all__'

class CmrSalamnSerializers(serializers.ModelSerializer):
    class Meta:
        model = CmrSalamn
        fields = '__all__'

class CmrBarjameSerializers(serializers.ModelSerializer):
    class Meta:
        model = CmrBarjame
        fields = '__all__'

class CmrFerdowsserializers(serializers.ModelSerializer):
    class Meta:
        model = CmrFerdows
        fields = '__all__'

class CmrMashahirSerializers(serializers.ModelSerializer):
    class Meta:
        model = CmrMashahir
        fields = '__all__'

class ContinerSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    document_type_name = serializers.CharField(source='document_type.name', read_only=True)
    bill_name = serializers.CharField(source='bill.bill_lading_number', read_only=True)
    bill_ship = serializers.CharField(source='bill.ship', read_only=True)
    carrier_name = serializers.CharField(source='carrier.name', read_only=True)
    truck_name = serializers.CharField(source='truck.License_plate_number', read_only=True)
    route_des = serializers.CharField(source='route.distinction_city', read_only=True)
    class Meta:
        model = Continer
        fields = ['file_number', 'number', 'invoice','size',
                'Date_receipt_documents','bill_name', 'bill', 'bill_ship','product_name', 
                'product_count','document_type_name','carrier_name', 
                'download_date','status','warehouse_receipt_date', 
                'national_id','weight_documents','weight_bascol', 
                'difference_weight','excess_tonnage','serial_number', 
                'route','truck_name','commission','fare_amount', 
                'advance_rent_amount','driver','contract_number', 
                'freeTime','description', 'route_des', 'file_number']
class continerPlusSerializers(serializers.ModelSerializer):
    bill_name = serializers.CharField(source='bill.bill_lading_number', read_only=True)
    bill_ship = serializers.CharField(source='bill.ship', read_only=True)
    bill_Owners_of_goods = serializers.CharField(source='bill.Owners_of_goods', read_only=True)
    class Meta:
        model = Continer
        fields = ['file_number', 'number', 'bill_name', 'bill_ship',
                'download_date', 'bill_Owners_of_goods', 'route']
class GuideSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'

class VolumeGuideSerializers(serializers.ModelSerializer):
    class Meta:
        model = VolumeGuide
        fields = '__all__'

class DemurrageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Demurrage
        fields = '__all__'

class ExitContinerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExitContiner
        fields = '__all__'

class MiscellaneousLoadSerializers(serializers.ModelSerializer):
    class Meta:
        model = MiscellaneousLoad
        fields = '__all__'
        
class LoadingFeesSerializers(serializers.ModelSerializer):
    cost_name = serializers.CharField(source='cost.name', read_only=True)
    cost_id = serializers.CharField(source='cost.id', read_only=True)

    class Meta:
        model = LoadingFees
        fields = ['id', 'continer', 'company', 'cost_name','cost_id' , 'date', 'fees', 'description']
 
class LogSerializers(serializers.ModelSerializer):
    booking_name = serializers.CharField(source='booking.booking_number', read_only=True)

    class Meta:
        model = Log
        fields = ['id','company', 'booking_name', 'status', 'update_status', 'continer_number',
                  'guide','loading_date', 
                  'guide','product_weight','carrier','route','truck','owners_of_goods', 
                  'rent','tonnageـweight','tonnage_count','tonnageـamount','commission_type', 
                  'commission_percent','commission_amount','total_amount_owners_of_goods', 
                  'company_info','driver','placedـnumber','rent_driver','tonnage_count_driver', 
                  'tonnageـamount_driver','portـcommission','parking','perrent_port', 
                  'total_amount_driver','driver_accountـbalance','difference','discribtion', 'update_date']


class GuideReportSerialzers(serializers.ModelSerializer):
    guide_serial = serializers.CharField(source='guide_id.name', read_only=True)

    class Meta:
        model = Guide
        fields = ['id',"company", 'is_active', 'guide_serial']

class SumFeesSerialzers(serializers.ModelSerializer):
    continer = ContinerSerializers(read_only=True) 
    class Meta:
        model = SumFees
        fields = ['id', 'continer', 'sum_fees']

class BookingLogSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class ContinerBookingSerializers(serializers.ModelSerializer):

    continers = serializers.SerializerMethodField()
    bills = serializers.SerializerMethodField()
    demurrage = serializers.SerializerMethodField()
    exit_continer = serializers.SerializerMethodField()
    sum_fees = serializers.SerializerMethodField()
    bookings = BookingSerializers(source='booking_set', many=True, read_only=True)
    class Meta:
        model = Guide
        fields = ["id", "company","continer","is_valid","guide_number","guide_id_salman",
                "guide_id_ferdows","guide_id_barjame","guide_id_mashahir","is_active","sender",
                "receiver","carrier","next_carrier","carrier_descriptions","place_date_delivery_goods",
                "location_date_loading","attached_documents","sign_number","download_info",
                "pure_agreements","sender_instructions","place_date_issue","date_place_receipt_goods",
                "confirm_date","bills", "bookings", "continers", "demurrage","exit_continer","sum_fees"] 

    def get_bills(self, obj):
        bills = BillDescribtion.objects.filter(continer__guide=obj).distinct()
        return BillDescribtionSeriallizer(bills, many=True).data

    def get_sum_fees(self, obj):
        fees = SumFees.objects.filter(continer__guide=obj).distinct()
        return SumFeesSerialzers(fees, many=True).data
    
    def get_continers(self, obj):
        continers = Continer.objects.filter(guide=obj).select_related('bill')
        return ContinerSerializers(continers, many=True).data
    
    def get_demurrage(self, obj):
        demurrage = Demurrage.objects.filter(continer__guide=obj).distinct()
        return DemurrageSerializers(demurrage, many=True).data
    
    def get_exit_continer(self, obj):
        exit_continer = ExitContiner.objects.filter(continer__guide=obj).distinct()
        return ExitContinerSerializers(exit_continer, many=True).data
    
class ContinerSumFeesSerializers(serializers.ModelSerializer):
    sum_fees = serializers.SerializerMethodField()

    class Meta:
        model = Continer
        fields = ['file_number', 'number', 'invoice','size',
                'Date_receipt_documents','bill', 'bill_ship','product', 
                'product_count','document_type','carrier', 
                'download_date','status','warehouse_receipt_date', 
                'national_id','weight_documents','weight_bascol', 
                'difference_weight','excess_tonnage','serial_number', 
                'route','truck','commission','fare_amount', 
                'advance_rent_amount','driver','contract_number', 
                'freeTime','description', 'route_des', 'file_number', 'sum_fees']

    def get_fees(self, obj):
        fees = SumFees.objects.filter(continer=obj)
        return SumFeesSerialzers(fees, many=True).data