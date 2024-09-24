import requests
import os
import argparse

from urllib.parse import urlparse
from save_images import download_image
from dotenv import load_dotenv


def main():
    load_dotenv()
    link_apod = 'https://api.nasa.gov/planetary/apod'

    parser = argparse.ArgumentParser(description='Сачивакет фотографии APOD запуска nasa')
    parser.add_argument('--folder',
                        type=str,
                        default='apod_nasa_images',
                        help='Введите имя папки в которую хотите поместить фотографии APOD nasa images:')

    args = parser.parse_args()
    apod_folder = args.folder

    os.makedirs(apod_folder, exist_ok=False)

    apod_key = os.getenv('NASA_KEY')

    count = 30 
    payload = {"count": count, "api_key": apod_key}
    
    response = requests.get(link_apod, params=payload)
    response.raise_for_status()
    links = response.json()

    for number, link in enumerate(links, 1):
        if 'url' in link:
            url = link['url']

            filename2 = urlparse(url)
            expansion = os.path.splitext(url)
            file_name = f'{filename2.netloc}_{number}{expansion[1]}'
            full_path = os.path.join(apod_folder, file_name)

            download_image(apod_folder, url, full_path)


if __name__ == "__main__":
    main()
