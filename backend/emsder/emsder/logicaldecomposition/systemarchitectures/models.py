from django.db import models
from basemodels.models import BaseModel

class SystemType(BaseModel):
    SYSTEM_TYPE_CHOICES =(
        ('Internal', 'Internal'),
        ('External', 'External'),
    )
    systemtype = models.CharField(max_length=10,
                                    choices=SYSTEM_TYPE_CHOICES,
                                    default = 'Internal')

class System(BaseModel):
    project = models.ForeignKey('projects.Project', related_name='systems', default=1, on_delete = models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    systemtype = models.ForeignKey(SystemType, unique=True, default=1, on_delete = models.SET_DEFAULT)
    description = models.TextField(blank=True, null=True)

    # Make it possible to create sub systems.
    system = models.ForeignKey('self', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    

    def __str__(self):
        return self.name
