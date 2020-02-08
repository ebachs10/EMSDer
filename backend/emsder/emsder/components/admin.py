from django.contrib import admin
from .models import Component, Manufacture, PiDiagram
from emsder.signals.models import Signal
from reversion.admin import VersionAdmin


class SignalInline(admin.StackedInline):
    model = Signal
    fields =('component', 'name', 'signalcategory', 'signalname', 'datatype')
    readonly_fields = ('signalname',)

class ComponentAdmin(VersionAdmin):
    #list_display = ['name', 'ManufactureName', 'typenumber','created_date', 'modified_date']
    list_display = ['ManufactureName', 'typenumber' , 'modified_date' , 'signals_count']
    fields = (('name', 'manufacture'), 'typenumber')

    inlines = [
        SignalInline        
    ]

    def ManufactureName(self, obj):
        return obj.manufacture.name
    ManufactureName.admin_order_field  = 'ManufactureName'  #Allows column order sorting     

class PiDiagram(VersionAdmin):
     list_display = ['project', 'system' , 'modified_date']   


admin.stie.register(PiDiagram)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Manufacture)