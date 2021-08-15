from __future__ import absolute_import, unicode_literals

from celery import Celery
from kombu import Exchange, Queue, binding

exchange = Exchange('douyin', type='topic')
celery_queue = [
    Queue(
        'my.queue.one',
        [binding(exchange=exchange, routing_key='my.routong.key')],
        queue_arguments={'x-queue-mode': 'lazy', 'x-max-priority': 10},
        max_priority=10
    )
]

app = Celery('proj',
             broker='amqp://guest:guest@localhost:5672/',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
