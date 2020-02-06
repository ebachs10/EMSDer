from django.db import models
from django.utils.timezone import now
from basemodels.models import BaseModel
from simple_history.models import HistoricalRecords

class SignalCategory(BaseModel):
    name = models.CharField(max_length=200) 
    alias = models.CharField(max_length=200)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

#class DataType(BaseModel):
#    name = models.CharField(max_length=200)
#    memoryspace = models.IntegerField()   
#
#
#    def __str__(self):
#        return self.name                

class Signal(BaseModel):
    name = models.CharField(max_length=200)
    component = models.ForeignKey('components.Component', related_name='signals', default=1, on_delete=models.CASCADE, blank=True, null=True)
    #interface = models.ForeignKey('interfaces.Interface', related_name='signals', default=1, on_delete=models.CASCADE, blank=True, null=True)
    signalcategory = models.ForeignKey(SignalCategory, default=1, on_delete = models.SET_DEFAULT, blank=True, null=True)
    datatype = models.ForeignKey('datatypes.Datatype', default=1, on_delete = models.SET_DEFAULT, blank=True, null=True)
    history = HistoricalRecords()

    @property
    def signalname(self):
        return "%s_%s" % (self.signalcategory.alias, self.name)

    def __str__(self):
        return self.name
