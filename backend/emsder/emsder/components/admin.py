from django.contrib import admin
from .models import Component, Manufacture, PiComponent
from emsder.signals.models import Signal, SignalAlarm
from reversion.admin import VersionAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class SignalAlarmInline(NestedStackedInline):
    model = SignalAlarm
    extra = 1
    fk_name = 'signal'

class SignalInline(NestedStackedInline):
    model = Signal
    extra = 1
    fk_name = 'component'
    inlines = [SignalAlarmInline]        

class ComponentAdmin(NestedModelAdmin):
    model = Component
    inlines = [SignalInline]           


admin.site.register(Component, ComponentAdmin)   

#class SignalInline(admin.StackedInline):
#    model = Signal
#    fields =('component', 'name', 'signalcategory', 'signalname', 'datatype')
#    readonly_fields = ('signalname',)
#    extra = 0
#
#class ComponentAdmin(VersionAdmin):
#    list_display = ['ManufactureName', 'typenumber' , 'modified_date' , 'signals_count']
#
#    inlines = [
#        SignalInline        
#    ]
#
#    def ManufactureName(self, obj):
#        return obj.manufacture.name
#    ManufactureName.admin_order_field  = 'ManufactureName'  #Allows column order sorting 
#
#class ComponentInline(admin.StackedInline):
#    model = Component
#    list_display = ['manufacture',]
#    extra = 0    
#
#class PiComponentAdmin(VersionAdmin):
#    list_display = ['name', 'component' , 'ManufactureName' , 'number_of_signals', 'system', 'modified_date']
#
#    readonly_fields = (['ManufactureName', 'number_of_signals'])
#
#    def ManufactureName(self, obj):
#        return obj.component.manufacture.name
#
#    def number_of_signals(self, obj):
#        return obj.component.signals_count             
   

#admin.site.register(PiComponent, PiComponentAdmin)
#admin.site.register(Component, ComponentAdmin)
#admin.site.register(Manufacture)

