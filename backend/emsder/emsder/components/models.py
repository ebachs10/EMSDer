from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords
from basemodels.models import BaseModel

class Manufacture(BaseModel):
    name = models.CharField(max_length=200) 
    history = HistoricalRecords()
    #component = models.ForeignKey(Component, related_name='manufacturer', on_delete=models.CASCADE)     

class Component(BaseModel):
    system = models.ForeignKey('systemarchitectures.System', related_name='components', default=1, on_delete = models.SET_DEFAULT)
    name = models.CharField(max_length=200, null=True)
    typenumber = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    manufacture = models.ForeignKey(Manufacture, default=1, on_delete = models.SET_DEFAULT)
    history = HistoricalRecords()

    def __str__(self):
        return self.typenumber


