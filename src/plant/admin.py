from django.contrib import admin

# Register your models here.
from .models import Plant, Device, EndPoint, TargetUri

admin.site.register(Plant)
admin.site.register(Device)
admin.site.register(EndPoint)
admin.site.register(TargetUri)
