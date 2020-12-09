import requests
import base64
import json
from upload import uploadinfo

def ocr():
        status = 'Exiting'
        IMAGE_PATH = 'picture.jpg'
        SECRET_KEY = 'sk_819d20dbf94c6fa082a4beaf'
        with open(IMAGE_PATH, 'rb') as image_file:
                img_base64 = base64.b64encode(image_file.read())

        url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=usa&secret_key=%s' % (SECRET_KEY)  #Replace 'ind' with  your country code
        r = requests.post(url, data = img_base64)
        try:
                print(r.json()['results'][0]['plate'])

        except:
                print("No number plate found")
                return
                
        plate = str(r.json()['results'][0]['plate'])
        uploadinfo(plate, status)



