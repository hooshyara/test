from django.contrib import admin
from .models import Permission, Group

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fields = ['user',
              'access','add_list_item','update_list','delete_list','delete_item', 
              'update_item','add_owner_of_goods','update_owner_of_goods', 
              'delete_owner_of_goods','add_rout','update_rout','delete_rout', 
              'add_station','update_station','delete_station','add_truck', 
              'update_truck','delete_truck','add_driver','update_driver', 
              'delete_driver','add_company','update_company','delete_company', 
              'add_demurrage','update_demurrage','delete_demurrage', 
              'add_warehousing','update_warehousing','delete_warehousing', 
              'users','add_bill','update_bill','disable_bill','add_continer', 
              'update_continer','delete_continer','manage_attachments', 
              'container_demurrage_management','booking_management','truck_exit', 
              'management_of_loading_costs', 
              'Upload_the_documents_attached_to_the_bill_of_lading', 
              'list_of_issued_bills_of_lading'
              ]
    
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    fields = []