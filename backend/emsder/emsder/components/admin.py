from django.contrib import admin
from .models import Signal, Component, Manufacture

#class SignalAdmin(admin.ModelAdmin):

#   fieldsets = [
#       ("Name", {'fields': ["name"]}),
#       ("Category", {'fields': ["category"]})
#   ]
#
#class ComponentAdmin(admin.ModelAdmin):
#
#    fieldsets = [
#        ("Type Number", {'fields': ["typenumber"]}),
#        ("Signals", {'fields': ["Signals"]})
#    ]


class SignalInline(admin.StackedInline):
    model = Signal

class ComponentAdmin(admin.ModelAdmin):
    inlines = [
        SignalInline
        
    ]

#admin.site.register(Signal, SignalAdmin)
admin.site.register(Component, ComponentAdmin)
#admin.site.register(Component)
admin.site.register(Signal)
admin.site.register(Manufacture)