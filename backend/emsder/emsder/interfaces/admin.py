from django.contrib import admin
from .models import Interface, BusType
from reversion.admin import VersionAdmin

class InterfaceAdmin(VersionAdmin):
    pass

class BusTypeAdmin(VersionAdmin):
    pass


admin.site.register(Interface, VersionAdmin)
admin.site.register(BusType, BusTypeAdmin)
