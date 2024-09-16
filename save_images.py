import requests 
import os

from urllib.parse import urlparse


def download_image(url, full_path):

    response = requests.get(url)
    response.raise_for_status()

    with open(full_path, 'wb') as file:
        file.write(response.content)

def get_extansion(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]
