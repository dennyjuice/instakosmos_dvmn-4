import os
from instabot import Bot

from fetch_spacex import get_latest_spacex_imgs
from fetch_hubble import download_hubble_collection_imgs
from upload_images import upload_images_to_instagram

from dotenv import load_dotenv

SPACEX_API = 'https://api.spacexdata.com/v3/launches/latest'
HUBBLE_API = 'http://hubblesite.org/api/v3'

def main():
  load_dotenv()
  login = os.environ['LOGIN']
  password = os.environ['PASSWORD']

  os.makedirs('images', exist_ok=True)

  get_latest_spacex_imgs(SPACEX_API)

  download_hubble_collection_imgs('printshop', HUBBLE_API)

  bot = Bot()
  bot.login(username=login, password=password)
  upload_images_to_instagram(bot)

if __name__ == "__main__":
  main()