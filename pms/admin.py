from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Building, Room

# Register your models here.

class BuildingAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'modified_at', 'description')
    list_display = ('name', 'address')
    search_fields = ('name', 'landmark_1', 'address')


class RoomAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'modified_at', 'name', 'description')
    list_display = ('flat_number', 'building', 'sqft_area', 'rent', 'ec_acc_number')
    search_fields = ('flat_number', 'building', 'sqft_area', 'rent', 'ec_acc_number')
    list_filter = ('flat_type',)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.site_title = 'Grexter Admin'
admin.site.site_header = 'Grexter Admin'
admin.site.index_title = 'GREXTER'

