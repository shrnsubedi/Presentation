from .celery import app
from time import sleep

@app.task
def add(x, y):
    sleep(5)
    return x+y

@app.task(bind=True)
def add_by_input(self):
    try:
        res=5+'5'
        return res
    except TypeError as exc:
        raise self.retry(exc=exc) 


@app.task
def mul(x, y):
    sleep(5)
    return x * y


@app.task
def xsum(numbers):
    sleep(5)
    return sum(numbers)