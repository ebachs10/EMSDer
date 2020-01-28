from django.contrib import admin
from .models import Signal, SignalCategory

class SignalAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Name", {'fields': ["name"]}),
        ("Category", {'fields': ["category"]})
    ]

admin.site.register(SignalCategory)
admin.site.register(Signal, SignalAdmin)

