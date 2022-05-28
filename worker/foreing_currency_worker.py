from core.utilities.thread_job import ThreadJob
from worker.worker import event, celery


@celery.task
def foreign_currency_worker_services():
    print("foreign currency workered")


foreign_currency_worker = ThreadJob(foreign_currency_worker_services, event, 2)
