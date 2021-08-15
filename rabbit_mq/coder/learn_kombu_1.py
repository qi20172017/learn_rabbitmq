from kombu import Connection
import datetime
 
# "amqp://guest:guest@localhost:5672//"中的amqp就是上文所提到的transport，
# 后面的部分是连接具体transport所需的参数，具体含义下篇博客中会讲到
with Connection('amqp://guest:guest@localhost:5672//') as conn:
    simple_queue = conn.SimpleQueue('simple_queue')
    message = 'helloword, sent at %s' % datetime.datetime.today()
    simple_queue.put(message)
    print('Sent: %s' % message)
    simple_queue.close()