import requests
import shutil
import json

class netclass():

    def myfirstCall():

        url = 'https://github.com/'
        r = requests.get('https://github.com/')
        print(r )
        print(r.contents)
        print(r.status_code)

    myfirstCall()

    def download_image(url,file_name)
        res = requests.get(uri,stream = True)
        if 200==res.status_code:
            with open(file_name, 'wb')as f:
                shutil.copyfileobj(res.raw, f)
            print('imagen descargada corectamente')
        else:
            print('No se encontro la imagen')
        

        def get_weather(self, city)
            api_key='69ec8ca2037d63a120d31c59efd0f605'
            base_url = 'httpp://api.openwathermap.org/data/2.5/wather'
            params={'q':city, 'appid'api_key,'units':'metric'}

            try:
                r=requests.get(base_url,params=params)
                r.raise_for_status()

                waether.data = r.json()
            if 200 == weather_data['cod']:
                print(f'Elclima en{weather_data['weather'][o]['description']}')
                print(f'Description{weather_data['main']['temp']}°c')
                print(f'humedad{weather_data['main']['humanidity']}%')
                print(f'Viento{wather_data[wird]}')
    
        


