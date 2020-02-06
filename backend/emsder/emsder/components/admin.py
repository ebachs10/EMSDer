from django.contrib import admin
from .models import Component, Manufacture
from emsder.signals.models import Signal


class SignalInline(admin.StackedInline):
    model = Signal
    fields =('component', 'name', 'signalcategory', 'signalname', 'datatype')
    readonly_fields = ('signalname',)

class ComponentAdmin(admin.ModelAdmin):
    #list_display = ['name', 'ManufactureName', 'typenumber','created_date', 'modified_date']
    list_display = ['name', 'ManufactureName', 'typenumber' , 'modified_date']
    fields = (('name', 'manufacture'), 'typenumber')

    inlines = [
        SignalInline        
    ]

    def ManufactureName(self, obj):
        return obj.manufacture.name
    ManufactureName.admin_order_field  = 'ManufactureName'  #Allows column order sorting     

admin.site.register(Component, ComponentAdmin)
admin.site.register(Manufacture)