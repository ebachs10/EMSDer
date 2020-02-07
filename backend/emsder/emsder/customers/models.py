from django.db import models
from basemodels.models import BaseModel
import reversion

@reversion.register()
class Customer(BaseModel):
    name = models.CharField(max_length=200)
    cvr = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
