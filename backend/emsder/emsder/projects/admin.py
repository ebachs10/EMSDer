from django.contrib import admin
from .models import Project
from reversion.admin import VersionAdmin

class ProjectAdmin(VersionAdmin):
    pass

admin.site.register(Project, ProjectAdmin)