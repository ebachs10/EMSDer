from django.contrib import admin
from .models import ProjectPreference
from reversion.admin import VersionAdmin

class ProjectPreferenceAdmin(VersionAdmin):
    pass

admin.site.register(ProjectPreference, ProjectPreferenceAdmin)
