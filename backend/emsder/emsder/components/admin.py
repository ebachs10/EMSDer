from django.contrib import admin
from .models import Component, Manufacture
from emsder.signals.models import Signal


class SignalInline(admin.StackedInline):
    model = Signal

class ComponentAdmin(admin.ModelAdmin):
    inlines = [
        SignalInline        
    ]

admin.site.register(Component, ComponentAdmin)
#admin.site.register(Component)
admin.site.register(Manufacture)