import requests 
import os
from urllib.parse import urlparse
from datetime import datetime


def download_image(url, full_path):

    response = requests.get(url)
    response.raise_for_status()

    with open(full_path, 'wb') as file:
        file.write(response.content)


def get_expansion(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]


def fetch_spacex_last_launch(url_nasa, name_folder):

    response = requests.get(url_nasa)
    response.raise_for_status()
    data = response.json()
    last_links = data.get('links', {}).get('flickr', {}).get('original', [])

    for url_number, last_nasa_url in enumerate(last_links):
        filename = f'spacex{url_number+1}.jpg'
        full_path = os.path.join(name_folder, filename)
        
        download_image(last_nasa_url, full_path)


def get_epic_nasa_images(folder_name, api_key):

    link_epic = "https://api.nasa.gov/EPIC/api/natural/image"

    links_count = 10
    params = {"api_key": api_key, "count": links_count}

    response = requests.get(link_epic, params=params)
    response.raise_for_status()
    epic_images = response.json()

    for epic_image in epic_images[:10]:
        file_name = epic_image["image"]
        epic_image_date = epic_image["date"]
    
        epic_image_date = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")
        link_path = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{file_name}.png?api_key={api_key}"
        path = os.path.join(folder_name, f'{file_name}.png')

        download_image(link_path, path)


def get_apod_nasa_images(api_key, name_folder):

    link_apod = 'https://api.nasa.gov/planetary/apod'

    count = 30 
    payload = {"count": count, "api_key": api_key}

    response = requests.get(link_apod, params=payload)
    response.raise_for_status()
    links = response.json()

    for number, link in enumerate(links):
        if 'url' in link:
            url = link['url']

            filename2 = urlparse(url)
            expansion = os.path.splitext(url)
            file_name = f'{filename2.netloc}_{number + 1}{expansion[1]}'
            full_path = os.path.join(name_folder, file_name)

            download_image(url, full_path)


def main():

    
    name_folder = 'images'

    api_key = ''
    nasa_api_key = ''

    url_nasa = f'https://api.spacexdata.com/v5/launches/{nasa_api_key}'

    if not os.path.exists(name_folder):
        os.makedirs(name_folder)

    get_epic_nasa_images(name_folder, api_key)
    fetch_spacex_last_launch(url_nasa, name_folder)
    get_apod_nasa_images(api_key, name_folder)
        

if __name__ == "__main__":
    main()
