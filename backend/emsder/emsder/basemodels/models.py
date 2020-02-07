from django.db import models
#from simple_history.models import HistoricalRecords

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)
 #   history = HistoricalRecords()

    class Meta:
        abstract = True