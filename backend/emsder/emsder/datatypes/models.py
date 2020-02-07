from django.db import models
from basemodels.models import BaseModel
import reversion

@reversion.register()
class DataType(BaseModel):
    datatype = models.CharField(max_length=200)
    memoryspace = models.IntegerField()
    lowerbound = models.IntegerField()
    upperbound = models.IntegerField()   

    def __str__(self):
        return self.datatype 

