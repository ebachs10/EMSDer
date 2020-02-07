from django.db import models
from basemodels.models import BaseModel
from simple_history.models import HistoricalRecords

#class GeneralPreferences(BaseModel):
#    pass

class ProjectPreference(BaseModel):
    CAMELCASE = 'CC'
    UNDERSCORE = 'US'
    SIGNAL_NAME_STYLE_CHOICES = [
        (CAMELCASE, 'camelCase'),
        (UNDERSCORE, 'underscore'),
    ]

    SCSNCN = 'SCSNCN' # signal class + signal name + component name
    SCCNSN = 'SCCNSN' # signal class + component name + signal name
    SIGNAL_NAME_CONCATENATION_CHOICES = [
        (SCSNCN, 'signal class + signal name + component name'),
        (SCCNSN, 'signal class + component name + signal name'),
    ]   

    signal_name_style = models.CharField(max_length=200, choices=SIGNAL_NAME_STYLE_CHOICES, default=UNDERSCORE,)
    signal_name_concatenation = models.CharField(max_length=200, choices=SIGNAL_NAME_CONCATENATION_CHOICES, default=SCSNCN,) # signal class + signal name + component name

    def __str__(self):
        return self.name

