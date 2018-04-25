#!/usr/bin/env python
import pika
import smtplib
import json
import credentials
import os

# Reading the credentials file
# sender = credentials.SENDER_EMAIL
# password = credentials.SENDER_PASSWORD
sender = os.environ['SENDER_EMAIL']
password = os.environ['SENDER_PASSWORD']

print(sender)
print(password)

# Setting up the CloudAMQP queue
# queue = 'UserRegistrationQueue'
queue = os.environ['QUEUE_NAME']

# queue_url = 'amqp://spbdyewq:0PfDzWG1GiXAe5pNVv4u6WPdl9qF60cf@eagle.rmq.cloudamqp.com/spbdyewq'
queue_url = os.environ['QUEUE_URL']


params = pika.URLParameters(queue_url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=queue, durable = True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    msg = body.decode("utf-8")
    msg = json.loads(msg)

    # toEmail = 'dscodetest@mailinator.com'
    # toEmail = os.environ['TO_EMAIL']

    toEmail = 'kanurocks19@gmail.com'
    
    birthday = msg['birthday']
    first_name = msg['firstName']
    cell = msg['cell']

    try:
        # Assuming service account is GMAIL
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        message = "Hi " + first_name + ",\n"
        message += "We have received your following details\n"
        message += "First name - " + first_name + "\n"
        message += "Birthday - " + birthday + "\n"
        message += "Mobile Phone - " + cell + "\n"
        print(message)
        server.sendmail(sender, toEmail, message)
        server.quit()
    except smtplib.SMTPException as e:
        print(str(e))
        server.quit()

channel.basic_consume(callback, queue=queue, no_ack=True)

print('[*] Waiting for messages:')
channel.start_consuming()