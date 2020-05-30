import requests
import os
from io import BytesIO

from PIL import Image
from PIL import ImageFile

from instabot import Bot

from dotenv import load_dotenv

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True # Чтобы убрать ошибку ValueError: Decompressed Data Too Large

load_dotenv()
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']

directory = 'images/'
spacex_api = 'https://api.spacexdata.com/v3/launches/latest'
hubble_api_image = 'http://hubblesite.org/api/v3/image/'
hubble_api_collection = 'http://hubblesite.org/api/v3/images/'
MAX_SIZE = (1080, 1080)


def fetch_spacex_last_launch(img_url, img_number):
  os.makedirs(directory, exist_ok=True)

  response = requests.get(img_url)
  response.raise_for_status()

  save_prepared_images(response, f'spacex-{img_number+1}.jpg')



def get_latest_spacex_imgs(url):
  response = requests.get(url)
  response.raise_for_status()
  spacex_imgs = response.json()['links']['flickr_images']

  for img_number, img in enumerate(spacex_imgs):
    img_url = spacex_imgs[img_number]
    fetch_spacex_last_launch(img_url, img_number)


def download_hubble_img(image_id):
  os.makedirs(directory, exist_ok=True)

  response = requests.get(hubble_api_image+image_id)
  response.raise_for_status()
  img_url = response.json()['image_files'][-1]['file_url']
  response = requests.get('http:'+img_url)
  response.raise_for_status()
  
  save_prepared_images(response, f'hubble-{image_id}.jpg')


def download_hubble_collection_imgs(collection):
  response = requests.get(hubble_api_collection+collection)
  response.raise_for_status()
  collection_list = response.json()

  for img_number, img in enumerate(collection_list):
    image_id = collection_list[img_number]['id']
    print('качаем - ',  image_id)
    download_hubble_img(str(image_id))


def save_prepared_images(response, filename):
  img = Image.open(BytesIO(response.content))
  # Добавил эту проверку потому-что некоторые картинки с хаблом имели прозрачный фон,
  # и при сохранении в jpeg он делался черным
  if img.mode == 'RGBA':
    img.load()
    background = Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])
    background.save(directory + filename, format="JPEG")
  else:
    img.thumbnail(MAX_SIZE)
    img.save(directory + filename, format="JPEG")



#get_latest_spacex_imgs(spacex_api)

#download_hubble_img('4646')

#download_hubble_collection_imgs('news')

bot = Bot()
bot.login(username=LOGIN, password=PASSWORD)
bot.upload_photo("images/hubble-4639.jpg", caption="Jupiter!")