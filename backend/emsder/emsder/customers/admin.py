from django.contrib import admin
from .models import Customer
from reversion.admin import VersionAdmin

class CustomerAdmin(VersionAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
