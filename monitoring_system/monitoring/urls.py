from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_screen'),
    path('start-task/', start_task_measurements, name='start_task_measurements'),
    path('test-task/', test_task_measurements, name='test_task_measurements'),
    path('test/', test, name='test'),
]