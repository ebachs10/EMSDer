from django.contrib import admin
from .models import DataType
from reversion.admin import VersionAdmin

class DataTypeAdmin(VersionAdmin):
    pass

admin.site.register(DataType, DataTypeAdmin)
