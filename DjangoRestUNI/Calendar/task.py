from celery import shared_task

@shared_task
def generate_date_events():
    print('Hola')

