from django.db import models
from django.utils import timezone


# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=200)
    plant_id = models.IntegerField(primary_key=True)
    interval = models.IntegerField(default=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DeviceType(models.IntegerChoices):
    INVERTER = 1
    SCB = 2
    EM = 3
    WS = 4
    MFM = 5


class Device(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    type = models.IntegerField(choices=DeviceType.choices)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    block_id = models.IntegerField()
    room_id = models.IntegerField()
    device_id = models.IntegerField()
    status = models.CharField(max_length=100, default="INIT")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EndPoint(models.Model):
    type = models.IntegerField(primary_key=True)
    endpoint = models.CharField(max_length=100)


class TargetUri(models.Model):
    type = models.IntegerField(choices=DeviceType.choices, primary_key=True)
    uri = models.CharField(max_length=200)
