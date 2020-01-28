from django.db import models

class SignalCategory(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Signal Categories"

    def __str__(self):
        return self.category

class Signal(models.Model):
    name = models.CharField(max_length=200) 
    category = models.ForeignKey(SignalCategory, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name

class Component(models.Model):
    typenumber = models.CharField(max_length=200)
    signals = models.ManyToManyField(Signal)

    def __str__(self):
        return self.typenumber

