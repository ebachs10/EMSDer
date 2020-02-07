from django.contrib import admin
from .models import System, SystemType
from reversion.admin import VersionAdmin

class SystemAdmin(VersionAdmin):
    pass

class SystemTypeAdmin(VersionAdmin):
    pass

admin.site.register(System)
admin.site.register(SystemType)
