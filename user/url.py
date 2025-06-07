from django.urls import path
from .views import UserView, LoginView, CheckUser, LogOutView

app_name = 'user'

urlpatterns = [
    path('', UserView.as_view(), name='get_all_user'),
    path('ed/<int:id>/', UserView.as_view(), name='edit_user'),
    path('log/', LoginView.as_view(), name='log'),
    path('check/', CheckUser.as_view(), name='check'),
    path('out/', LogOutView.as_view(), name='out'),

]