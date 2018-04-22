#!/usr/bin/env python
import pika

url = 'amqp://spbdyewq:0PfDzWG1GiXAe5pNVv4u6WPdl9qF60cf@eagle.rmq.cloudamqp.com/spbdyewq'
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='q', durable = 'false')

def callback(ch, method, properties, body):
  print(" [x] Received %r" % body)

channel.basic_consume(callback, queue='q',no_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()