from django.db import models
from django.utils.timezone import now

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True

def __str__(self):
    return self.created_date

class Manufacture(BaseModel):
    name = models.CharField(max_length=200) 
    #component = models.ForeignKey(Component, related_name='manufacturer', on_delete=models.CASCADE)    

class SignalCategory(BaseModel):
    name = models.CharField(max_length=200) 
    #component = models.ForeignKey(Component, related_name='manufacturer', on_delete=models.CASCADE)    

class Component(BaseModel):
    name = models.CharField(max_length=200, null=True)
    typenumber = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    manufacture = models.OneToOneField(Manufacture, default=1, on_delete = models.SET_DEFAULT)
    #signal

    def __str__(self):
        return self.typenumber
  

class Signal(BaseModel):
    name = models.CharField(max_length=200)
    component = models.ForeignKey(Component, related_name='signals', default=1, on_delete=models.CASCADE)
    signalcategory = models.OneToOneField(SignalCategory, default=1, on_delete = models.SET_DEFAULT)

    def __str__(self):
        return self.name


