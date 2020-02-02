from django.db import models
from basemodels.models import BaseModel

class NetworkArchitecture(BaseModel):
    project = models.ForeignKey('projects.Project', related_name='networkarchitecture', default=1, on_delete = models.SET_DEFAULT)
    name = models.CharField(max_length=200) 
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name
