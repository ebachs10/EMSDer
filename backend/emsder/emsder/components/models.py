from django.db import models

class Manufacture(models.Model):
    name = models.CharField(max_length=200) 
    #component = models.ForeignKey(Component, related_name='manufacturer', on_delete=models.CASCADE)    

class SignalCategory(models.Model):
    name = models.CharField(max_length=200) 
    #component = models.ForeignKey(Component, related_name='manufacturer', on_delete=models.CASCADE)    

class Component(models.Model):
    typenumber = models.CharField(max_length=200)
    manufacture = models.OneToOneField(Manufacture, default=1, on_delete = models.SET_DEFAULT)

    def __str__(self):
        return self.typenumber
  

class Signal(models.Model):
    name = models.CharField(max_length=200)
    component = models.ForeignKey(Component, related_name='signals', default=1, on_delete=models.CASCADE)
    signalcategory = models.OneToOneField(SignalCategory, default=1, on_delete = models.SET_DEFAULT)

    def __str__(self):
        return self.name


