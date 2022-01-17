from celery import shared_task
# from celery.schedules import crontab
# from celery.decorators import periodic_task
from .api.v1.views import get_exchange_rate

@shared_task
def celery_get_exchange_rate():
    get_exchange_rate()

# @periodic_task(
#     run_every=(crontab(minute='*/1')),
#     name="celery_get_exchange_rate",
#     ignore_result=True
# )
# def celery_get_exchange_rate():
#     QuoteView.get_exchange_rate()