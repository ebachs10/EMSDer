from django.db import models
from django.utils.timezone import now
from basemodels.models import BaseModel
import reversion

@reversion.register()
class Manufacture(BaseModel):
    name = models.CharField(max_length=200) 
    #component = models.ForeignKey(Component, related_name='manufacturer', on_delete=models.CASCADE)     

@reversion.register()
class Component(BaseModel):
    system = models.ForeignKey('systemarchitectures.System', related_name='components', default=1, on_delete = models.PROTECT)
    name = models.CharField(max_length=200, null=True)
    typenumber = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    manufacture = models.ForeignKey(Manufacture, default=1, on_delete = models.SET_DEFAULT)

    def __str__(self):
        return self.typenumber


