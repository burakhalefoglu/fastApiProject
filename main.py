import uvicorn
from fastapi import FastAPI
import pyximport

pyximport.install()
from service.dependency_resolver import ioc_container as service
from worker import worker

service.inject_dependencies()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    worker.start_workers()  # its async and non blocked
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
