from django.db import models
from basemodels.models import BaseModel
import reversion

@reversion.register
class BusType(BaseModel):
    SYSTEM_TYPE_CHOICES =[
    ('EtherCAT', 'EtherCAT'),
    ('PROFINET', 'PROFINET '),
    ]

    bustype = models.CharField(
        max_length=50,
        choices=SYSTEM_TYPE_CHOICES,
        default = 'EtherCAT',
    )

@reversion.register
class Interface(BaseModel):
    name = models.CharField(max_length=200)
    bustype = models.ForeignKey(BusType, default=1, on_delete = models.PROTECT)
    samplerate = models.IntegerField()

    def __str__(self):
        return self.bustype
    


