from django.urls import path
from .views import *

app_name = 'tariff'

urlpatterns = [
    path('', TariffView.as_view(), name='tarrif'),
    path('ed/<int:id>/', TariffView.as_view(), name='edit_tarrif'),
    path('wa/', WarehousingTariffView.as_view(), name='wa'),
    path('wa/<int:id>/', WarehousingTariffView.as_view(), name='edit_wa'),
]