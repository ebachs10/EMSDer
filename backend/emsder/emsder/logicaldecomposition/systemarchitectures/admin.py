from django.contrib import admin
from .models import System, SystemType
from reversion.admin import VersionAdmin

class SystemAdmin(VersionAdmin):
    list_display = [
        'name', 
        'project', 
        'SystemTypeName',
        ]

    def SystemTypeName(self, obj):
        return obj.systemtype.systemtype
        SystemTypeName.admin_order_field  = 'SystemTypeName'  #Allows column order sorting           

class SystemTypeAdmin(VersionAdmin):
    pass

admin.site.register(System, SystemAdmin)
admin.site.register(SystemType)
