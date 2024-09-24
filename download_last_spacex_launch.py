import requests
import os
import argparse

from save_images import download_image
from dotenv import load_dotenv


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Это скрипт download_last_spacex_launch.py в переменную epic_key введите свай наса-ключ и запустите скрип: download_last_spacex_launch.py --folder (имя папки в которую хотите скачать фото)')
    parser.add_argument('--folder',
                        type=str,
                        default='last_spacex_launch_images',
                        help='Введите имя папки в которую хотите поместить фотографии:')
    
    args = parser.parse_args()
    folder_last_launch = args.folder

    if not os.path.exists(folder_last_launch):
        os.makedirs(folder_last_launch)

    launch_id = os.getenv('LAST_LAUNCH_KEY')

    url_nasa = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(url_nasa)
    response.raise_for_status()
    last_launch_links = response.json()['links']['flickr']['original']

    for url_number, last_nasa_url in enumerate(last_launch_links, 1):
        filename = f'spacex{url_number}.jpg'
        full_path = os.path.join(folder_last_launch, filename)

        download_image(folder_last_launch, last_nasa_url, full_path)


if __name__ == "__main__":
    main()
