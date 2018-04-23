#!/usr/bin/env python
import pika
import smtplib
import json

sender = 'kanurocks19@gmail.com'
password = "@2Kushagra"
# receivers = ['to@todomain.com']
queue = 'UserRegistrationQueue2'

url = 'amqp://spbdyewq:0PfDzWG1GiXAe5pNVv4u6WPdl9qF60cf@eagle.rmq.cloudamqp.com/spbdyewq'
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=queue, durable = True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # print(type(body))
    msg = body.decode("utf-8")
    msg = json.loads(msg)
    # {"firstName":"Kushagra","birthday":"0001-01-01","email":"kushagra.agarwal@nyu.edu","cell":"234","password":"ddvr"}
    toEmail = msg['email']
    birthday = msg['birthday']
    firstName = msg['firstName']
    cell = msg['cell']

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        message = "Hi " + firstName + ",\n\
        We have received your following details\n\
        First name - " + firstName + "\n\
        Birthday - " + birthday + "\n\
        Mobile Phone - " + cell + "\n\
        Regards,\n\
        Kushagra Agarwal"
        # print(message)
        server.sendmail(sender, toEmail, message)
        server.quit()
    except smtplib.SMTPException as e:
        print(str(e))
        server.quit()

channel.basic_consume(callback, queue=queue, no_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()