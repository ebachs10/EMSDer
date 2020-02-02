from django.db import models
from django.utils.timezone import now
from basemodels.models import BaseModel

class SignalCategory(BaseModel):
    name = models.CharField(max_length=200) 
    alias = models.CharField(max_length=200)

    def __str__(self):
        return self.name       

class Signal(BaseModel):
    name = models.CharField(max_length=200)
    component = models.ForeignKey('components.Component', related_name='signals', default=1, on_delete=models.CASCADE)
    signalcategory = models.OneToOneField(SignalCategory, default=1, on_delete = models.SET_DEFAULT)

    @property
    def signalname(self):
        return self.name

    def __str__(self):
        return self.name
