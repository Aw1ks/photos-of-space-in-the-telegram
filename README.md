# Sending photos of us to the telegram channel
This project takes links to photos from the official NASA website using the API key (which will be sent to your email) and sends it to the telegram channel.
## How to install
This project uses libraries such as: [os](https://docs.python.org/3/library/os.html), [random](https://python-scripts.com/random?ysclid=m0zhzk6iqx773448571), [argparse](https://docs.python.org/3/library/argparse.html), [dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [telegram](https://timeweb.cloud/tutorials/python/kak-sozdat-telegram-bota-na-python), [time](https://pythonru.com/osnovy/modul-time-v-python?ysclid=m0zjkf98rz969569317), [dotenv](https://python.plainenglish.io/managing-api-keys-and-secrets-in-python-using-the-dotenv-library-a-beginners-guide-33890401cd15), [requests](https://python-scripts.com/requests?ysclid=lyr2i4f3us982315000), [datetime](https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python?ysclid=m0zjls6tc6502083556) and [urllib.parse](https://docs.python.org/3/library/urllib.parse.html).

API keys can be obtained on the [NASA website](https://api.nasa.gov/). To do this, go to the [NASA website](https://api.nasa.gov/) and create a key, after creating the key, you will receive it by email. The api key will look something like this: `o7235hHi9wg873035UHJdshig`

Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To save the data from prying eyes, we will create an .env file in which we will place: TG_TOKEN, TG_CHAT_ID, NASA_KEY.
Let's do it this way: 
```
TG_TOKEN = 'the token of your telegram bot'
TG_CHAT_ID = 'telegram token of the channel you want to send messages to (must start with -100)'
NASA_KEY = 'api key that you will receive'
```
# Launch example
## Change the folder name
To change the name of the folder where the photos will be saved, you need to call the argument when running the script and specify the name of the package
```
python download_apod_nasa.py --folder (the name of any folder you want to put the photo)
```
it works for all scripts that download photos.
## How to launch a script download_apod_nasa
This file downloads the launch APOD photos and downloads them to the folder you specify. To run this code, you need to run the script itself.
```
python download_apod_nasa.py
```
## How to launch a script download_epic_nasa
This file downloads the EPIC launch photos and downloads them to the folder you specify. To run this code, you need to run the script itself.
```
python download_epic_nasa.py
```
## How to launch a script download_last_spacex_launch
This file downloads photos of the last NASA launch and downloads them to the folder you specify. To run this code, you need to run the script itself.
```
python download_last_spacex_launch.py
```
## How to launch a script tg_bot.py
To run this script, you need to run it and additionally call two arguments. The first is the folder in which you select the folder where the photos are stored. The second is the time in which you record the interval between sending photos.
```
python tg_bot.py --folder (the name of the folder from which you want to send the photo) --time(the time interval between sending the photo)
```
It is important to note that the time period is counted in seconds.

You can also run this script without the time argument, then the interval between sending the photo will be 4 hours.
```
python tg_bot.py --folder (the name of the folder from which you want to send the photo)
```
# Environment variables
Environment variables are key—value pairs that determine the settings and behavior of the operating system and programs. You can read more here [Learn more about environment variables](https://habr.com/ru/companies/gnivc/articles/792082/)
## Environment variables in download_last_spacex_launch.py
The launch_id variable takes the ID of the last launch from the .env file using the [os](https://docs.python.org/3/library/os.html) library using the `.getenv` method.
```
launch_id = os.getenv('LAST_LAUNCH_KEY')
```
## Environment variables in download_epic_nasa.py and download_apod_nasa.py
The situation here is exactly the same as with download_last_spacex_launch.py The epic_key and apod_key variables store the NASA api key.

download_apod_nasa.py
```
apod_key = os.getenv('NASA_KEY')
```
download_epic_nasa.py
```
epic_key = os.getenv('NASA_KEY')
```
