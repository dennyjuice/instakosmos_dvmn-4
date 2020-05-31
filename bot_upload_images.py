from instabot import Bot
import os
import time

def bot_upload_images(bot):
    images_list = []
    img_path ='images/'

    images_list = os.listdir(img_path)
    images_list = list(filter(lambda x: x.endswith('.jpg'), images_list))
    print(images_list)

    try:
        for pic in images_list:

            print("upload: " + pic)
            pic_name = '.'.join(pic.split('.')[:-1])
            print(pic_name)

            bot.upload_photo(img_path+pic, caption=pic_name)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
                # snd msg
                break

            time.sleep(30)

    except Exception as e:
        print(str(e))