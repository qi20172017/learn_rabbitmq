from kombu import Connection
 
with Connection('amqp://guest:guest@localhost:5672//') as conn:
    simple_queue = conn.SimpleQueue('kwai.live.count')
    # simple_queue = conn.SimpleQueue('simple_queue')

    len = simple_queue.qsize()
    # message = simple_queue.get(block=True, timeout=1)
    # print("Received: %s" % message.payload)
    print(len)
    # message.ack()
    simple_queue.close()