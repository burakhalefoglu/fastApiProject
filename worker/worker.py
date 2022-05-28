import aioschedule as schedule
import asyncio
import time
import threading
import time


from core.utilities.thread_job import ThreadJob
from worker.bist_worker import BistWorker
from worker.emtia_worker import EmtiaWorker
from worker.foreing_currency_worker import ForeignCurrencyWorker




async def job():
    await asyncio.sleep(1)
    print("I'm running on thread %s" % threading.current_thread())

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()






def run_schedules():
    bist = BistWorker()
    emtia = EmtiaWorker()
    foreign = ForeignCurrencyWorker()

    # schedule.every().day.at("22:56").do(foreign.foreign_currency_worker_services)
    # schedule.every().day.at("22:56").do(emtia.emtia_worker_services)
    # schedule.every().day.at("22:56").do(bist.bist_worker_services)


    # schedule.every(1).seconds.do(run_threaded, job)
    # schedule.every(2).seconds.do(run_threaded, job)
    # schedule.every(3).seconds.do(run_threaded, job)
    # schedule.every(1).seconds.do(run_threaded, job)
    # schedule.every(1).seconds.do(run_threaded, job)


    schedule.every(1).seconds.do(foreign.foreign_currency_worker_services)
    schedule.every(2).seconds.do(emtia.emtia_worker_services)
    schedule.every(3).seconds.do(bist.bist_worker_services)


 
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        loop.run_until_complete(schedule.run_pending())

        time.sleep(0.1)


def start_workers():
    job = ThreadJob(run_schedules)
    job.deamon = True
    job.start()


