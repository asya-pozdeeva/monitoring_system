# import os
# from celery import Celery
# from celery.schedules import crontab
#
#
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'monitoring_system.settings')
#
# app = Celery('monitoring_system')
# app.config_from_object('django.conf:settings', namespace="CELERY")
# app.autodiscover_tasks()
#
#
#
# # заносим таски в очередь
# app.conf.beat_schedule = {
#     'log-measurements-every-minute': {
#         'task': 'monitoring.tasks.log_measurements',
#         'schedule': crontab(),# по умолчанию выполняет каждую минуту
#     },
#
# }
