from django.db import models
from django.utils import timezone

# Create your models here.

class KeyModel(models.Model):

    username = models.CharField(max_length=30)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class MasterModel(models.Model):

    key = models.ForeignKey(KeyModel, on_delete = models.CASCADE)
    master = models.CharField(max_length=30)

    def __str__(self):
        return self.master

class DetailModel(models.Model):

    master = models.ForeignKey(MasterModel, on_delete = models.CASCADE)
    detail = models.CharField(max_length=30)

    def __str__(self):
        return self.detail