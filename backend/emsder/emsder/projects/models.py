from django.db import models
from basemodels.models import BaseModel

class Project(BaseModel):
    name = models.CharField(max_length=200)
    identification_number = models.DecimalField(max_digits=4, decimal_places=0) 
    #customer = models.OneToOneField('customers.Customer', default=1, on_delete = models.SET_DEFAULT)
    customer = models.ForeignKey('customers.Customer', related_name='customer', unique=True, default=1, on_delete = models.SET_DEFAULT)
    subcontractor = models.ForeignKey('customers.Customer', related_name='subcontractor', unique=True, default=1, on_delete = models.SET_DEFAULT)
    #subcontractor = models.OneToOneField('customers.Customer', default=1, on_delete = models.SET_DEFAULT)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


