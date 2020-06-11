import requests
from prepare_images import save_prepared_image

def download_hubble_collection_imgs(collection, url):
  response = requests.get(f'{url}/images/{collection}')
  response.raise_for_status()
  collections = response.json()

  for img_number, img in enumerate(collections):
    image_id = collections[img_number]['id']
    
    response = requests.get(f'{url}/image/{image_id}')
    response.raise_for_status()
    img_url = response.json()['image_files'][-1]['file_url']
    response = requests.get(f'http:{img_url}')
    response.raise_for_status()

    save_prepared_image(response, f'hubble-{image_id}.jpg')