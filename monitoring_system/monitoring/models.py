from django.db import models
from django.contrib.auth.models import User

class Condition(models.Model):
    min_temperature = models.IntegerField(null=False)
    max_temperature = models.IntegerField(null=False)
    min_humidity = models.IntegerField(null=False)
    max_humidity = models.IntegerField(null=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Condition(min_temp={self.min_temperature}, max_temp={self.max_temperature}, min_humidity={self.min_humidity}, max_humidity={self.max_humidity})'

class Location(models.Model):
    name_location = models.CharField(max_length=255)
    conditions = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='locations')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name_location

class Sensor_type(models.Model):
    types = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.types} ({self.unit})'

class Sensor(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='sensors')
    sensor_type = models.ForeignKey(Sensor_type, on_delete=models.CASCADE, related_name='sensor_type')
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Sensor({self.sensor_type} at {self.location})'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Measurement({self.value} from {self.sensor} at {self.timestamp})'


class Alert(models.Model):
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='alerts')
    conditions = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='alerts')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Alert for {self.measurement} - Condition: {self.conditions} at {self.timestamp}'


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reports')
    time_start = models.TimeField()
    time_stop = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report by {self.user} for {self.location} from {self.time_start} to {self.time_stop}'
