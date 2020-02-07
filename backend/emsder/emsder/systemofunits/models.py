from django.db import models
from basemodels.models import BaseModel
import reversion

@reversion.register()
class UnitPrefix(BaseModel):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10)
    base10 = models.IntegerField()
    decimal = models.IntegerField()
    englishwordshort = models.CharField(max_length=30)
    englishwordlong = models.CharField(max_length=50)

@reversion.register()
class SiUnit(BaseModel):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    baseunit = models.CharField(max_length=200)
    otherunit = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

@reversion.register()
class NonSiUnit(BaseModel):
    name = models.CharField(max_length=200)
    siunit = models.ForeignKey(SiUnit, unique=True, default=1, on_delete = models.SET_DEFAULT)
    convertion = models.FloatField()

    def __str__(self):
        return self.name    
