from django.forms import ModelForm
from django.db import models
from .models import Device, Plant


class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'plant_id', 'interval']


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'type', 'plant_id', 'block_id', 'room_id', 'device_id']
