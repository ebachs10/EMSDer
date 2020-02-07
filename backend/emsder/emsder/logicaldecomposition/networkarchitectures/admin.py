from django.contrib import admin
from .models import NetworkArchitecture
from reversion.admin import VersionAdmin

class NetworkArchitectureAdmin(VersionAdmin):
    pass

admin.site.register(NetworkArchitecture, NetworkArchitectureAdmin)
