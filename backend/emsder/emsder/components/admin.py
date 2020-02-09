from django.contrib import admin
from .models import Component, Manufacture, PiComponent
from emsder.signals.models import Signal
from reversion.admin import VersionAdmin


class SignalInline(admin.StackedInline):
    model = Signal
    fields =('component', 'name', 'signalcategory', 'signalname', 'datatype')
    readonly_fields = ('signalname',)
    extra = 0

class ComponentAdmin(VersionAdmin):
    #list_display = ['name', 'ManufactureName', 'typenumber','created_date', 'modified_date']
    list_display = ['ManufactureName', 'typenumber' , 'modified_date' , 'signals_count']
    fields = (('manufacture'), 'typenumber')

    inlines = [
        SignalInline        
    ]

    def ManufactureName(self, obj):
        return obj.manufacture.name
    ManufactureName.admin_order_field  = 'ManufactureName'  #Allows column order sorting 

class ComponentInline(admin.TabularInline):
    #list_display = ['ManufactureName', 'typenumber']
    model = Component
    list_display = ['typenumber',]
    extra = 0    
class PiComponentAdmin(VersionAdmin):
     list_display = ['project', 'system' , 'modified_date']



admin.site.register(PiComponent, PiComponentAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Manufacture)