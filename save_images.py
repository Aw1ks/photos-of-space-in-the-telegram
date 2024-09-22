import os
from pathlib import Path

import requests
from urllib.parse import urlparse


def download_image(folder, url, filename, api_key=''):
    
    Path(folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=api_key)
    response.raise_for_status()
    full_path = os.path.join(folder, filename)
    
    with open(full_path, 'wb') as file:
        file.write(response.content)


def get_extansion(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]
