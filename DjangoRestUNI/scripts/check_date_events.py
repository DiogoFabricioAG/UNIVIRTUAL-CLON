import django
import os
import sys

from datetime import timedelta
from django.utils import timezone
import datetime
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","DjangoRestUNI.settings")
django.setup()

from Calendar.models import Event
from Notification.models import Notification

today = datetime.date.today().strftime('%Y/%m/%d')

allEvents = Event.objects.all()
for event in allEvents:
    if event.date_event.strftime('%Y/%m/%d') == today:
        Notification.objects.create(send_to=event.user,typenotification = f'El dia del evento "{event.title}" ha llegado.')




