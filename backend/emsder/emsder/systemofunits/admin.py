from django.contrib import admin
from .models import UnitPrefix, NonSiUnit, SiUnit
from reversion.admin import VersionAdmin

class UnitPrefixAdmin(VersionAdmin):
    pass

class NonSiUnitAdmin(VersionAdmin):
    pass

class SiUnitAdmin(VersionAdmin):
    pass

admin.site.register(UnitPrefix, UnitPrefixAdmin)
admin.site.register(NonSiUnit, NonSiUnitAdmin)
admin.site.register(SiUnit, SiUnitAdmin)
