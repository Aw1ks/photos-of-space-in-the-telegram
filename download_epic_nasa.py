import requests
import os
import argparse

from datetime import datetime
from save_images import download_image
from dotenv import load_dotenv


def main():
    load_dotenv()
    epic_link = "https://api.nasa.gov/EPIC/api/natural/images"

    parser = argparse.ArgumentParser(description='Введите название папки в которую хотите скачать фотографии EPIC фото:')
    parser.add_argument('--folder',
                        type=str,
                        default='epic_nasa_images',
                        help='Введите имя папки в которую хотите поместить фотографии EPIC nasa images:')

    args = parser.parse_args()
    epic_folder = args.folder

    os.makedirs(epic_folder, exist_ok=False)
    
    epic_key = os.getenv('NASA_KEY')

    params = {"api_key": epic_key}

    response = requests.get(epic_link, params=params)
    response.raise_for_status()
    epic_images = response.json()

    params = {
        'api_key': epic_key
    }

    for epic_image in epic_images[:10]:
        file_name = epic_image["image"]
        epic_image_date = epic_image["date"]

        epic_image_date = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")
        link_path = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{file_name}.png"
        link_path_with_params = f'{link_path}?{urlencode(params)}'
        path = os.path.join(epic_folder, f'{file_name}.png')

        download_image(link_path_with_params, path)


if __name__ == "__main__":
    main()
