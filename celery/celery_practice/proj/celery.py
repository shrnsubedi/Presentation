from celery import Celery

BROKER_URL='amqps://raljkjvq:TIL4sL3FQiN5J2b64RE-y-WLhhYOt2rq@chimpanzee.rmq.cloudamqp.com/raljkjvq'
BACKEND_URL='db+sqlite:///db.sqlite3'

app = Celery('proj',
             broker=BROKER_URL,
             backend=BACKEND_URL,
             include=['proj.tasks'])

app.conf.update(
    result_expires=3600,
    #task_routes = {
    #    'proj.tasks.add': {'queue': 'hipri'},
    #},

)

app.conf.beat_schedule={
    'mul-every-10-seconds':{
        'task':'proj.tasks.mul',
        'schedule':10.0,
        'args':(16,16)
    }
}

if __name__ == '__main__':
    app.start()