# DoSomethingConsumer
A consumer script that fetches the items from the CloudAMQP queue and send the information to a service account (dscodetest@mailinator.com)

## Installation
pip install -r requirements.txt

## Running
After installation the can can be run locally or on a server. Since we have to run this app continuously, I have hosted it on heroku.

## Open Issues
* Script is currently not checking if the email is successfully sent or not which will result in loss of message from the queue
