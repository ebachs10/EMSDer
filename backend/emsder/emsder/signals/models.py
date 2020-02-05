from django.db import models
from django.utils.timezone import now
from basemodels.models import BaseModel

class SignalCategory(BaseModel):
    name = models.CharField(max_length=200) 
    alias = models.CharField(max_length=200)

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
    component = models.ForeignKey('components.Component', related_name='signals', default=1, on_delete=models.CASCADE)
    signalcategory = models.ForeignKey(SignalCategory, unique=True, default=1, on_delete = models.SET_DEFAULT)
    datatype = models.ForeignKey('datatypes.Datatype', unique=True, default=1, on_delete = models.SET_DEFAULT, blank=True)

    @property
    def signalname(self):
        return "%s_%s" % (self.signalcategory.alias, self.name)

    def __str__(self):
        return self.name
