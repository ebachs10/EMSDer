from django.db import models
from django.utils.timezone import now
from basemodels.models import BaseModel
import reversion

@reversion.register()
class SignalCategory(BaseModel):
    name = models.CharField(max_length=200) 
    alias = models.CharField(max_length=200)

    def __str__(self):
        return self.name
               
@reversion.register()
class Signal(BaseModel):
    name = models.CharField(max_length=200)
    component = models.ForeignKey('components.Component', related_name='signals', default=1, on_delete=models.CASCADE, blank=True, null=True)
    #interface = models.ForeignKey('interfaces.Interface', related_name='signals', default=1, on_delete=models.CASCADE, blank=True, null=True)
    signalcategory = models.ForeignKey(SignalCategory, default=1, on_delete = models.SET_DEFAULT, blank=True, null=True)
    datatype = models.ForeignKey('datatypes.Datatype', default=1, on_delete = models.SET_DEFAULT, blank=True, null=True)

    @property
    def signalname(self):
        return "%s_%s" % (self.signalcategory.alias, self.name)

    def __str__(self):
        return self.name


@reversion.register()
class ProjectAlarmLevel(BaseModel):        
    alias = models.CharField(max_length=200) # e.g Slow, Fast, Coast 

    @property
    def level(self):
        return 1

@reversion.register()
class SignalAlarm(BaseModel):   
    signal = models.ForeignKey(Signal, related_name='signalalarm', default=1, on_delete=models.PROTECT, blank=True, null=True)
    autoreset = models.BooleanField() 
    description = models.CharField(max_length=200, blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)

    lowervalue = models.FloatField(blank=True, null=True)
    currentvalue = models.FloatField() # Remember to include check that its between lower and upper
    uppervalue =models.FloatField(blank=True, null=True)

    lowerdelay = models.FloatField(blank=True, null=True)
    currentdelay = models.FloatField(blank=True, null=True)
    upperdelay = models.FloatField(blank=True, null=True)
    


    

