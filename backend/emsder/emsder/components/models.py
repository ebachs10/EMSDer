from django.db import models
from django.utils.timezone import now
from basemodels.models import BaseModel
import reversion

@reversion.register()
class Manufacture(BaseModel):
    name = models.CharField(max_length=200) 
    #component = models.ForeignKey(Component, related_name='manufacturer', on_delete=models.CASCADE) 
    # 
    # 
@reversion.register()
class ComponentClass(BaseModel):
    name = models.CharField(max_length=200)         

@reversion.register()
class Component(BaseModel):

   #name = models.CharField(max_length=200, null=True, blank=True)
    project = models.ForeignKey('projects.Project', related_name='components', default=1, on_delete = models.PROTECT, null = True, blank = True)
    system = models.ForeignKey('systemarchitectures.System', related_name='components', default=1, on_delete = models.PROTECT, null=True, blank=True)
    componentclass = models.ForeignKey(ComponentClass, on_delete = models.PROTECT, null=True, blank=True)
    typenumber = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    manufacture = models.ForeignKey(Manufacture, on_delete = models.PROTECT)
    picomponent = models.ForeignKey('PiComponent', related_name='components',    default=1, on_delete = models.PROTECT, null = True, blank = True)

    @property
    def signals_count(self):
        if self.signals is not None and self.signals.count() > 0:
            return self.signals.count()
        return None    

    def __str__(self):
        return self.typenumber

@reversion.register()
class PiComponent(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    project = models.ForeignKey('projects.Project', related_name='picomponent', on_delete = models.PROTECT)
    system = models.ForeignKey('systemarchitectures.System', unique=True, related_name='picomponent', default=1, on_delete = models.PROTECT)
    #components = models.ForeignKey(Component, on_delete = models.PROTECT, null=True, blank=True)
    #components = models.ManyToManyField(Component)
    
    def __unicode__(self):
        return self.name

#@reversion.register()
#class PiDiagram(BaseModel):
#    name = models.CharField(max_length=200, null=True, blank=True)
#
#    
#    def __unicode__(self):
#        return self.name        