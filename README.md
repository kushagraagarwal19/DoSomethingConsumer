# DoSomethingConsumer
A consumer script that fetches the items from the CloudAMQP queue and send the information to a service account (dscodetest@mailinator.com)

## Installation
pip install -r requirements.txt

## Running
After installation the can can be run locally or on a server. Since we have to run this app continuously, I have hosted it on heroku. But, as Gmail's SMTP servers were not allowing to login. To overcome this, for the time being, I have allowed [less secure apps](https://support.google.com/accounts/answer/6010255) to access my gmail account.

The script is getting username, password, queue URL from the environment variables saved in the heroku. Whenever a message is queued, that message is transmitted to the email address (dscodetest@mailinator.com)

## Open Issues
* Script is currently not checking if the email is successfully sent or not which will result in loss of message from the queue
