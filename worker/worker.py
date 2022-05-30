import aioschedule as schedule
import asyncio
import threading
import time

from core.utilities.thread_job import ThreadJob
from worker.bist_worker import BistWorker
from worker.emtia_worker import EmtiaWorker
from worker.foreing_currency_worker import ForeignCurrencyWorker


async def job():
    await asyncio.sleep(1)
    print("I'm running on thread %s" % threading.current_thread())


def run_schedules():
    bist = BistWorker()
    emtia = EmtiaWorker()
    foreign = ForeignCurrencyWorker()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    schedule.every().day.at("20:30").do(foreign.foreign_currency_worker_services)
    schedule.every().day.at("19:30").do(emtia.emtia_worker_services)
    schedule.every().day.at("19:00").do(bist.bist_worker_services)

    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(0.1)


def start_workers():
    threadJob = ThreadJob(run_schedules)
    threadJob.deamon = True
    threadJob.start()
