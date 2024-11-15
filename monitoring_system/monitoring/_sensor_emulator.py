import numpy as np
import pickle
import os

class Sensor:
    """Клас эмулятор сенсора"""

    def __init__(self, id, base, amplitudes, frequencies, time_interval=0.1):
        self.id = id
        self.base = base
        self.amplitudes = amplitudes
        self.frequencies = frequencies
        self.time_interval = time_interval
        self.time_step = 0

    def generate_signal(self):
        t = self.time_step * self.time_interval
        signal = self.base + sum(A * np.sin(2 * np.pi * F * t) for A, F in zip(self.amplitudes, self.frequencies))
        self.time_step += 1
        return signal

def save_sensors_to_file(sensors, filename='sensors.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(sensors, f)

def load_sensors_from_file(filename='sensors.pkl'):
    with open(filename, 'rb') as f:
        sensors = pickle.load(f)
    return sensors

# # Создание сенсоров
# sensors = [
#       Sensor(id=1, base=20, amplitudes=[5, 2], frequencies=[0.1, 0.05]),
#       Sensor(id=2, base=40, amplitudes=[3, 1], frequencies=[0.15, 0.07]),
#       Sensor(id=3, base=2, amplitudes=[3, 1], frequencies=[0.2, 0.05]),
#       Sensor(id=4, base=60, amplitudes=[3, 1], frequencies=[0.25, 0.17]),
#     ]
#
# # Сохранение
# save_sensors_to_file(sensors)

# Загрузка
sensors = load_sensors_from_file()

def get_measurement(sensor_id):
    for sensor in  sensors:
        if int(sensor_id) == int(sensor.id):
            return sensor.generate_signal()
    else:
        return None