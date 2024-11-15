from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import OuterRef, Subquery, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Sensor, Measurement, Location
from .tasks import task_measurements



def index(request):
    # Последниие измерения
    latest_measurements = Measurement.objects.filter(sensor=OuterRef('pk')).order_by('-timestamp')

    # Получаем все локации с предзагруженными сенсорами и их последними измерениями
    locations = Location.objects.prefetch_related('sensors').annotate(
        sensors_with_last_measurement=Subquery(
            latest_measurements.values('value')[:1]
        )
    )
    translation = {
        "humidity": "Влажность",
        "temperature": "Температура"
    }

    context = {
        'locations': locations,
        'translation': translation
    }
    return render(request, 'monitoring/index.html', context)

def test(request):

    return HttpResponse()


def start_task_measurements(request):
    task_measurements()  # Запускаем задачу
    return HttpResponse("Задача запланированна!")

def test_task_measurements(request):
    task_measurements()  # Выполнить измерения
    return HttpResponse("Задача выполнена!")