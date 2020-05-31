import os
from instabot import Bot

from fetch_spacex import get_latest_spacex_imgs
from fetch_hubble import download_hubble_collection_imgs
from bot_upload_images import bot_upload_images

from dotenv import load_dotenv

load_dotenv()
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']

spacex_api = 'https://api.spacexdata.com/v3/launches/latest'
hubble_api = 'http://hubblesite.org/api/v3/'

if __name__ == "__main__":
  os.makedirs('images/', exist_ok=True)

  get_latest_spacex_imgs(spacex_api)

  download_hubble_collection_imgs('printshop', hubble_api)

  bot = Bot()
  bot.login(username=LOGIN, password=PASSWORD)

  bot_upload_images(bot)