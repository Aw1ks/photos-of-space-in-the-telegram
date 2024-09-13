import os
import random
import argparse
import telegram
import time

from dotenv import load_dotenv


def send_document(folder, bot, tg_chat_id, time_period):
    while True:
        all_files = []

        for root, _, files in os.walk(folder):
            all_files.extend([os.path.join(root, file) for file in files])

        if not all_files:
            print(f'В папке {folder} нет файлов.')
            break

        random_file = random.choice(all_files)

        try:
            with open(random_file, 'rb') as file:
                bot.send_document(chat_id=tg_chat_id, document=file)
                print(f'Отправлена фотография: {random_file}')

        except telegram.error.TelegramError as e:
            print(f'Произошла ошибка при отправке: {e}')

        time.sleep(time_period)


def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')

    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser(description='Отправка случайных фотографий в чат Telegram')
    parser.add_argument('--folder',
                        type=str,
                        default='folder',
                        help='Путь к папке, содержащей фотографии для отправки')
    parser.add_argument('--time',
                        type=int,
                        default=14400,
                        help='Введите промежуток времени между отправкой фотографий (В СЕКУНДАХ)')

    args = parser.parse_args()
    folder = args.folder
    time_period = args.time

    send_document(folder, bot, tg_chat_id, time_period)


if __name__ == '__main__':
    main()