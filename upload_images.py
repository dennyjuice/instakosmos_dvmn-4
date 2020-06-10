from instabot import Bot
import os
import time
from pathlib import Path
import logging

def upload_images_to_instagram(bot):
    images = []
    img_path = Path.cwd() / 'images'

    images = os.listdir(img_path)
    images = list(filter(lambda x: x.endswith('.jpg'), images))

    for pic in images:
        try:
            pic_name = '.'.join(pic.split('.')[:-1])

            bot.upload_photo(img_path / pic, caption=pic_name)
            if bot.api.last_response.status_code != 200:
                logging.error(bot.api.last_response)
                # snd msg
                break

            time.sleep(30)

        except Exception as e:
            logging.error(str(e))