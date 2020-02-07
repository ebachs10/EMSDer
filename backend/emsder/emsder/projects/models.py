from django.db import models
from basemodels.models import BaseModel
import reversion

@reversion.register()
class Project(BaseModel):
    name = models.CharField(max_length=200)
    identification_number = models.DecimalField(max_digits=4, decimal_places=0) 
    #customer = models.OneToOneField('customers.Customer', default=1, on_delete = models.SET_DEFAULT)
    customer = models.ForeignKey('customers.Customer', related_name='customer', default=1, on_delete = models.SET_DEFAULT, blank=True, null=True)
    subcontractor = models.ForeignKey('customers.Customer', related_name='subcontractor', default=1, on_delete = models.SET_DEFAULT, blank=True, null=True)
    #subcontractor = models.OneToOneField('customers.Customer', default=1, on_delete = models.SET_DEFAULT)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


