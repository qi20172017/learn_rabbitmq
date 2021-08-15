import requests
from kombu import Connection
# broker_url = 'amqp://guest:guest@localhost:5672/'
broker_url = 'amqp://admin:123456@192.168.1.62:5672/'
# queue = 'celery'
queue = 'kwai.spider.work.update_4'
with Connection(broker_url) as conn:

    simple_queue = conn.SimpleQueue(
        name=queue,
        queue_args={'x-queue-mode': 'lazy', 'x-max-priority': 10}

    )
    queue_size = simple_queue.qsize()
    simple_queue.close()
print(queue_size)