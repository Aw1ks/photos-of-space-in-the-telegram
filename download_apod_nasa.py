import requests
import os
import argparse

from urllib.parse import urlparse
from save_images import download_image
from dotenv import load_dotenv


def main():
    load_dotenv()
    link_apod = 'https://api.nasa.gov/planetary/apod'

    parser = argparse.ArgumentParser(description='Введите название папки в которую хотите скачать фотографии APOD фото:')
    parser.add_argument('--folder',
                        type=str,
                        default='apod_nasa_images',
                        help='Введите имя папки в которую хотите поместить фотографии APOD nasa images:')

    args = parser.parse_args()
    apod_folder = args.folder

    if not os.path.exists(apod_folder):
        os.makedirs(apod_folder)

    apod_key = os.getenv('NASA_KEY')

    count = 30 
    payload = {"count": count, "api_key": apod_key}
    
    response = requests.get(link_apod, params=payload)
    response.raise_for_status()
    links = response.json()

    for number, link in enumerate(links, start=1):
            url = link.get('url')
            if not url:
               continue

            apod_filename = urlparse(url).netloc
            expansion = os.path.splitext(url)[1]
            file_name = f'{apod_filename}_{number}{expansion}'
            full_path = os.path.join(apod_folder, file_name)

            download_image(url, full_path)


if __name__ == "__main__":
    main()
