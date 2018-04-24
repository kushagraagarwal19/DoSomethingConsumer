# DoSomethingConsumer
A consumer script that fetches the items from the CloudAMQP queue and send the information to a service account (dscodetest@mailinator.com)

## Installation
pip install -r requirements.txt

## Running
After installation the can can be run locally or on a server. Since we have to run this app continuously, I have hosted it on heroku. But, as Gmail's SMTP servers were not allowing to login, I have stopped that. So it's better to run this locally.

Add the username and password in the the [credentials.py](credentials.py) and change the SMTP server link and port in [consumer.py](consumer.py) and you are all set.

## Open Issues
* Script is currently not checking if the email is successfully sent or not which will result in loss of message from the queue
