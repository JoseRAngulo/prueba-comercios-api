from django.db import models

class BusinessType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BusinessSubType(models.Model):
    description = models.CharField(max_length=100)
    type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Business(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    owner_name = models.CharField(max_length=50)
    address = models.TextField()
    types = models.ManyToManyField(BusinessSubType)

    def __str__(self):
        return self.name