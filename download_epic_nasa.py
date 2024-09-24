import requests
import os
import argparse

from datetime import datetime
from save_images import download_image
from dotenv import load_dotenv
from urllib.parse import urlencode


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Скачивает фотографии EPIC запуска nasa')
    parser.add_argument('--folder',
                        type=str,
                        default='epic_nasa_images',
                        help='Введите имя папки в которую хотите поместить фотографии EPIC nasa images:')

    args = parser.parse_args()
    epic_folder = args.folder

    os.makedirs(epic_folder, exist_ok=False)

    nasa_token = os.getenv('NASA_KEY')

    payload = {'api_key': nasa_token}
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    nasa_epic_answers = response.json()

    for answer_number, answer in enumerate(nasa_epic_answers, 1):
        file_name = f'epic_{answer_number}.png'
        date = answer['date'].split()[0]
        date = date.split('-')
        name = answer['image']
        epic_image_link = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{name}.png'

        download_image(epic_folder, epic_image_link, file_name, payload)


if __name__ == "__main__":
    main()
