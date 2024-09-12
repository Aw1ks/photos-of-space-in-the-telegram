# Sending photos of us to the telegram channel
This project takes links to photos from the official NASA website using the API key (which will be sent to your email) and sends it to the telegram channel.
## How to install
API keys can be obtained on the NASA website. To do this, go to the NASA website and create a key, after creating the key, you will receive it by email. The api key will look something like this: `o7235hHi9wg873035UHJdshig`

Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

It is recommended to use
create a `.env` file in the project folder and hide all your tokens and keys in it:
```
TG_TOKEN = 'the token of your telegram bot'
TG_CHAT_ID = 'telegram token of the channel you want to send messages to (must start with -100)'
NASA_KEY = 'api key that you will receive'
```
