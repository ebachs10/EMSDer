from django.contrib import admin
from .models import UnitPrefix, NonSiUnit, SiUnit

admin.site.register(UnitPrefix)
admin.site.register(NonSiUnit)
admin.site.register(SiUnit)
