from ._sensor_emulator import *
from .filters import MovingAverager
from background_task import background


filters = {}
@background(schedule=60)
def task_measurements():
    from .models import Sensor, Measurement
    log_name = 'Log: Task_measurements: '
    print(log_name + 'Sensor polling')
    sensors = Sensor.objects.all()

    FILTER_PERIOD = 10

    for sensor in sensors:
        if sensor.id not in filters:
            filters[sensor.id] = MovingAverager(FILTER_PERIOD)

        measurement_value = get_measurement(sensor.id)
        if measurement_value is not None:
            filtered_value = filters[sensor.id].filter_value(measurement_value)
            Measurement.objects.create(sensor=sensor, value=filtered_value)
        else:
            print(f"{log_name} Sensor {sensor.id} is not connected.")
