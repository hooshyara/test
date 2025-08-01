from django.urls import path
from .views import *

app_name = 'booking'

urlpatterns = [
    path('', OwnersOfGoodsView.as_view(), name='owners_of_goods'),
    path('ed/<int:id>/', OwnersOfGoodsView.as_view(), name='OwnersOfGoods'),
    path('sailing/', SailingView.as_view(), name='Sailing'),
    path('sailing/<int:id>/', SailingView.as_view(), name='Sailing-edit'),
    path('bill/', BillDescribtionView.as_view(), name='bill'),
    path('bill/<int:id>/', BillDescribtionView.as_view(), name='bill-edit'),
    path('bill/<str:name>/', BillDescribtionView.as_view(), name='bill-edit'),
    path('route/', RouteView.as_view(), name='route'),
    path('route/<int:id>/', RouteView.as_view(), name='route-edit'),
    path('station/', StationView.as_view(), name='station'),
    path('station/<int:id>/', StationView.as_view(), name='station-edit'),
    path('driver/', DriverView.as_view(), name='driver'),
    path('driver/<int:id>/', DriverView.as_view(), name='driver-edit'),
    path('insurance/', InsuranceView.as_view(), name='insurance'),
    path('insurance/<int:id>/', InsuranceView.as_view(), name='insurance-edit'),
    path('carrier/', CarrierView.as_view(), name='carrier'),
    path('carrier/<int:id>/', CarrierView.as_view(), name='carrier-edit'),
    path('truckt/', TruckTypeView.as_view(), name='truckt'),
    path('truckt/<int:id>/', TruckTypeView.as_view(), name='truckt-edit'),
    path('truck/', TruckView.as_view(), name='truck'),
    path('truck/<int:id>/', TruckView.as_view(), name='truck-edit'),
    path('trailer/', TrailerView.as_view(), name='trailer'),
    path('trailer/<int:id>/', TrailerView.as_view(), name='trailer-edit'),
    path('packet/', PackagingTypeView.as_view(), name='packet'),
    path('packet/<int:id>/', PackagingTypeView.as_view(), name='packet-edit'),
    path('cmr/', DeliveryRecipientCMRView.as_view(), name='cmr'),
    path('cmr/<int:id>/', DeliveryRecipientCMRView.as_view(), name='cmr-edit'),
    path('dp/', DeliveryRecipientProductView.as_view(), name='dp'),
    path('dp/<int:id>/', DeliveryRecipientProductView.as_view(), name='dp-edit'),
    path('bi/', DeliveryRecipientBillView.as_view(), name='bi'),
    path('bi/<int:id>/', DeliveryRecipientBillView.as_view(), name='bi-edit'),
    path('city/', CityView.as_view(), name='city'),
    path('city/<int:id>/', CityView.as_view(), name='city-edit'),
    path('country/', CountryView.as_view(), name='country'),
    path('country/<int:id>/', CountryView.as_view(), name='country-edit'),
    path('product/', ProductView.as_view(), name='product'),
    path('product/<int:id>/', ProductView.as_view(), name='product-edit'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('booking/<int:id>/', BookingView.as_view(), name='booking-edit'),
    path('crbooking/<int:id>/', CreateBookingView.as_view(), name='booking-create'),
    path('douct/', GetDocumentTypeView.as_view(), name='douct'),
    path('douct/<int:id>/', GetDocumentTypeView.as_view(), name='douct-edit'),
    path('enter/', EnterTypeView.as_view(), name='enter'),
    path('enter/<int:id>/', EnterTypeView.as_view(), name='enter-edit'),
    path('post/', PostalCompanyView.as_view(), name='post'),
    path('post/<int:id>/', PostalCompanyView.as_view(), name='post-edit'),
    path('cost/', CostListView.as_view(), name='cost'),
    path('cost/<int:id>/', CostListView.as_view(), name='cost-edit'),
    path('dem/', DemurrageTypeView.as_view(), name='dem'),
    path('dem/<int:id>/', DemurrageTypeView.as_view(), name='dem-edit'),
    path('salman/', CmrSalamnView.as_view(), name='salman'),
    path('salman/<int:id>/', CmrSalamnView.as_view(), name='salman-edit'),
    path('barjame/', CmrBarjameView.as_view(), name='barjame'),
    path('barjame/<int:id>/', CmrBarjameView.as_view(), name='barjame-edit'),
    path('ferdows/', CmrFerdowsView.as_view(), name='ferdows'),
    path('ferdows/<int:id>/', CmrFerdowsView.as_view(), name='ferdows-edit'),
    path('mashhir/', CmrMashahirView.as_view(), name='mashhir'),
    path('mashhir/<int:id>/', CmrMashahirView.as_view(), name='mashhir-edit'),
    path('guide/', GuideView.as_view(), name='guide'),
    path('guide/<int:id>/', GuideView.as_view(), name='guide'),
    path('guideP/<int:id>/', GuidePluse.as_view(), name='guide'),
    path('vguide/', VolumeGuideView.as_view(), name='volumeGuide'),
    path('vguide/<int:id>/', VolumeGuideView.as_view(), name='volumeGuide'),
    path('demurrage/<int:id>/', DemurrageView.as_view(), name='demurrage'),
    path('demurrage/', DemurrageView.as_view(), name='demurrage'),
    path('continer/', ContinerView.as_view(), name='ContinerView'),
    path('continer/<int:id>/', ContinerView.as_view(), name='ContinerView'),
    path('exit/<int:id>/', ExitContinerView.as_view(), name='exit-ed'),
    path('exit/', ExitContinerView.as_view(), name='exit'),
    path('mi/<int:id>/', MiscellaneousLoadView.as_view(), name='mi'),
    path('la/<int:id>/', LoadingFeesView.as_view(), name='la-ed'),
    path('la/', LoadingFeesView.as_view(), name='la'),
    path('log/<int:id>/', LogView.as_view(), name='log'),
    path('log/', LogView.as_view(), name='log-ed'),
    path('guideReport/', GuideReportView.as_view(), name='gr'),
    path('bookingCreate/<int:id>/', BookingCreateView.as_view(), name='br'),
    path('continerCreate/<int:id>/', CreateContinerView.as_view(), name='creatCR'),
    path('sla/<int:id>/', SumFeesView.as_view(), name='sla'),
    path('continerbooking/<int:id>/', ContinerBookingView.as_view(), name='sla'),
    path('continerbookingInfo/<int:id>/', ContinerBookingInfoView.as_view(), name='slsa'),
    path('search/', ContinerBookingView.as_view(), name='ssla'),
    path('pdf/', GenerateReportPDF.as_view(), name='Generate-Report-PDF'),
    
]