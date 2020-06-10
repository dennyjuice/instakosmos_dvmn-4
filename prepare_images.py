from PIL import Image
from io import BytesIO
from pathlib import Path
import logging

MAX_SIZE = (1080, 1080)


def save_prepared_image(response, filename):
  try:
    img = Image.open(BytesIO(response.content))
    image_path =  Path.cwd() / 'images' / filename
      # Добавил эту проверку потому-что некоторые картинки с хаблом имели прозрачный фон,
      # и при сохранении в jpeg он делался черным
    if img.mode == 'RGBA':
      img.load()
      background = Image.new("RGB", img.size, (255, 255, 255))
      background.paste(img, mask=img.split()[3])
      background.thumbnail(MAX_SIZE)
      background.save(image_path, format="JPEG")
    else:
      img.thumbnail(MAX_SIZE)
      img.save(image_path, format="JPEG")
  except Exception:
    logging.warning('Ошибка загрузки картинки. Пропускаем')
    pass