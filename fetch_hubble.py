import requests
from prepare_images import save_prepared_images

def download_hubble_collection_imgs(collection, url):
  response = requests.get(url+'images/'+collection)
  response.raise_for_status()
  collection_list = response.json()

  for img_number, img in enumerate(collection_list):
    image_id = collection_list[img_number]['id']
    print('качаем - ',  image_id)
    
    response = requests.get(url+'image/'+f'{image_id}')
    response.raise_for_status()
    img_url = response.json()['image_files'][-1]['file_url']
    response = requests.get('http:'+img_url)
    response.raise_for_status()

    save_prepared_images(response, f'hubble-{image_id}.jpg')