from core.utilities.thread_job import ThreadJob
from worker.worker import event, celery


@celery.task
def emtia_worker_services():
    print("emtia workered")


emtia_worker = ThreadJob(emtia_worker_services, event, 2)




