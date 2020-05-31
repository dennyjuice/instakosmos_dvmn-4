from PIL import Image
from io import BytesIO

MAX_SIZE = (1080, 1080)

def save_prepared_images(response, filename):
  try:
    img = Image.open(BytesIO(response.content))
      
      # Добавил эту проверку потому-что некоторые картинки с хаблом имели прозрачный фон,
      # и при сохранении в jpeg он делался черным
    if img.mode == 'RGBA':
      img.load()
      background = Image.new("RGB", img.size, (255, 255, 255))
      background.paste(img, mask=img.split()[3])
      background.thumbnail(MAX_SIZE)
      background.save('images/' + filename, format="JPEG")
    else:
      img.thumbnail(MAX_SIZE)
      img.save('images/' + filename, format="JPEG")
  except Exception:
    print('Ошибка загрузки картинки. Пропускаем')
    pass