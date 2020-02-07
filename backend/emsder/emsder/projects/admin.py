from django.contrib import admin
from .models import Project
from reversion.admin import VersionAdmin
from django.db.models import Count

class ProjectAdmin(VersionAdmin):
    def get_queryset(self, request):
        qs = super(ProjectAdmin, self).get_queryset(request)
        return qs.annotate(subcontractors_count=Count('subcontractor'))

    def subcontractors_count(self, inst):
        return inst.subcontractors_count


    list_display = ['name', 'subcontractors_count']


admin.site.register(Project, ProjectAdmin)