from django.urls import path
from .views import *

app_name = 'permission'

urlpatterns = [
    path('', PermissionView.as_view(), name='perm'),
    path('<int:id>/', PermissionView.as_view(), name='perm'),
    path('group/', GroupView.as_view(), name='group'),
    path('group/<int:id>/', GroupView.as_view(), name='group-edit'),
]