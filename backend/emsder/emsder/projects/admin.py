from django.contrib import admin
from .models import Project
from reversion.admin import VersionAdmin
from django.db.models import Count

class ProjectAdmin(VersionAdmin):
    list_display = ('name', 'show_subcontractor_count')

    def get_queryset(self, request):
        qs = super(ProjectAdmin, self).get_queryset(request)
        return qs.annotate(subcontractor_count=Count('subcontractors'))

    def show_subcontractor_count(self, inst):
        return inst.subcontractor_count

    show_subcontractor_count = 'subcontractor_count'

admin.site.register(Project, ProjectAdmin)