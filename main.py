import uvicorn
from fastapi import FastAPI
import pyximport

pyximport.install()
from core.cross_cutting_concerns.logger.logger import init_inform_log, init_debug_log
from worker.emtia_worker import emtia_worker_services
from worker.foreing_currency_worker import foreign_currency_worker_services
from service.dependency_resolver import ioc_container as service
from worker.worker import celery

init_debug_log()
init_inform_log()
service.inject_dependencies()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 1 seconds.
    sender.add_periodic_task(1.0, emtia_worker_services.s(), name='add every 10')

    # Calls test('world') every 3 seconds
    sender.add_periodic_task(3.0, foreign_currency_worker_services.s(), expires=10)

    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


if __name__ == "__main__":
    # worker.start_workers(bist_worker,
    #                      foreign_currency_worker,
    #                      emtia_worker)  # its async and non blocked

    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
