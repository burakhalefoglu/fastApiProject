import threading

from celery import Celery
from celery.schedules import crontab

from core.utilities.thread_job import ThreadJob

event = threading.Event()


def start_workers(*jobs: ThreadJob):
    for j in jobs:
        j.start()


def date_obj_to_str(element: int) -> str:
    if element <= 9:
        return "0" + str(element)
    return str(element)


celery = Celery()
