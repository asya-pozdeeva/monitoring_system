from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.urls import reverse
from .models import Condition, Location, Sensor, Measurement, Alert, Report, Sensor_type

admin.site.register(Condition)
admin.site.register(Location)
admin.site.register(Measurement)
admin.site.register(Alert)
admin.site.register(Report)
admin.site.register(Sensor_type)
admin.site.register(Sensor)