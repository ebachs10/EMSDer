from django.db import models
from basemodels.models import BaseModel

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

class Interface(BaseModel):
    name = models.CharField(max_length=200)
    bustype = models.OneToOneField(BusType, default=1, on_delete = models.SET_DEFAULT)
    samplerate = models.IntegerField()

    def __str__(self):
        return self.bustype
    


