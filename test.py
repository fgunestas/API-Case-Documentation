import requests
import json
import base64
import requests
import json
import base64
from PIL import Image
from io import BytesIO
from diffusers.utils import load_image
# Hedef URL
#url = 'http://192.168.1.37:32703/api/custom_endpoint'
url = 'http://95.70.170.173:32703/api/Ad_Generator'

# Gönderilecek veri
#logo=load_image('sample.png')
prompt="a cup of coffee"
sample = {
        'Image_': ('sample.png', open('sample.png', 'rb'), 'image/png'),
        'Logo': ('logo.png', open('logo.png', 'rb'), 'image/png')
    }
data = {'Prompt':"a cup of coffee",
            'Renk1':"#81d8d0",
            'Renk2':"#81d8d0",
            'Punchline':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'Button':'Click Me'
    }

#prompt={'prompt':"a cup of coffee"}
#hex={'hex':"#81d8d0"}
response = requests.post(url, files=sample,data=data)

# Yanıtı kontrol et
if response.status_code == 200:
    # Başarılı yanıt
    api_response_image = Image.open(BytesIO(response.content))
    api_response_image.save('api_response_image.png')
    print("API'den dönen resim başarıyla kaydedildi.")
else:
    # Hata durumunda hata mesajını yazdır
    print(f"Hata kodu: {response.status_code}, Hata mesajı: {response.text}")

#response.save('APIresponsePng.png')