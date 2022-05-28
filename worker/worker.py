import threading
import schedule

from core.utilities.thread_job import ThreadJob
from bist_worker import bist_worker_services
from emtia_worker import emtia_worker_services
from foreing_currency_worker import foreign_currency_worker_services

event = threading.Event()


def run_schedules():
    # schedule.every().day.at("22:00").do(foreign_currency_worker_services)
    # schedule.every().day.at("22:00").do(emtia_worker_services)
    # schedule.every().day.at("22:00").do(bist_worker_services)

    schedule.every(1).seconds.do(emtia_worker_services)
    schedule.every(2).seconds.do(bist_worker_services)

    while True:
        schedule.run_pending()


def start_workers():
    job = ThreadJob(run_schedules)
    job.deamon = True
    job.start()


def date_obj_to_str(element: int) -> str:
    if element <= 9:
        return "0" + str(element)
    return str(element)
