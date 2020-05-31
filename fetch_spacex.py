import requests
from prepare_images import save_prepared_images

def fetch_spacex_last_launch(img_url, img_number):

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