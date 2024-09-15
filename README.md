# Sending photos of us to the telegram channel
This project takes links to photos from the official NASA website using the API key (which will be sent to your email) and sends it to the telegram channel.
## How to install
API keys can be obtained on the [NASA website](https://api.nasa.gov/). To do this, go to the [NASA website](https://api.nasa.gov/) and create a key, after creating the key, you will receive it by email. The api key will look something like this: `o7235hHi9wg873035UHJdshig`

Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
This project also uses libraries such as: [os](https://docs.python.org/3/library/os.html), [random](https://python-scripts.com/random?ysclid=m0zhzk6iqx773448571), [argparse](https://docs.python.org/3/library/argparse.html), [dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [telegram](https://timeweb.cloud/tutorials/python/kak-sozdat-telegram-bota-na-python), [time](https://pythonru.com/osnovy/modul-time-v-python?ysclid=m0zjkf98rz969569317), [dotenv](https://python.plainenglish.io/managing-api-keys-and-secrets-in-python-using-the-dotenv-library-a-beginners-guide-33890401cd15), [requests](https://python-scripts.com/requests?ysclid=lyr2i4f3us982315000), [datetime](https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python?ysclid=m0zjls6tc6502083556) and [urllib.parse](https://docs.python.org/3/library/urllib.parse.html).

It is recommended to use

create a `.env` file in the project folder and hide all your tokens and keys in it:
```
TG_TOKEN = 'the token of your telegram bot'
TG_CHAT_ID = 'telegram token of the channel you want to send messages to (must start with -100)'
NASA_KEY = 'api key that you will receive'
```
## Launch example
script number one: download_apod_nasa.py
```
python download_apod_nasa.py --folder (the name of the folder where you want to put the photo)
```

script number two: download_epic_nasa.py
```
python download_epic_nasa.py --folder (the name of the folder where you want to put the photo)
```

script number three: download_last_spacex_launch.py
```
python download_last_spacex_launch.py --folder (the name of the folder where you want to put the photo)
```

script number four: tg_bot.py
```
python tg_bot.py --folder (the name of the folder you want to take the photo from) --time (the time interval between sending the photo)
```
