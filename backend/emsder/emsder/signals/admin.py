from django.contrib import admin
from .models import Signal, SignalCategory
from reversion.admin import VersionAdmin

class SignalAdmin(VersionAdmin):
    pass

class SignalCategoryAdmin(VersionAdmin):
    pass

admin.site.register(Signal, SignalAdmin)
admin.site.register(SignalCategory, SignalCategoryAdmin)
