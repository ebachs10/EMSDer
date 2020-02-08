from django.db import models
from basemodels.models import BaseModel
import reversion

@reversion.register()
class Project(BaseModel):
    name = models.CharField(max_length=200)
    identification_number = models.DecimalField(max_digits=4, decimal_places=0) 
    customer = models.ForeignKey('customers.Customer', related_name='customer', default=1, on_delete = models.PROTECT, blank=True, null=True)
    subcontractor = models.ForeignKey('customers.Customer', related_name='subcontractor', default=1, on_delete = models.PROTECT, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    @property
    def systems_count(self):
        if self.systems is not None and self.systems.count() > 0:
            return self.systems.count()
        return None # or -1 or something that tells that there are no movements
    
    def __str__(self):
        return self.name


