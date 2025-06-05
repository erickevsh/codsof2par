from hashlib import md5
from requests import get
from datetime import datetime as datt

class RestMarvel:
  timestamp = datt.now().strftime('%Y-%d%H:%M:%S')
  pub_key = 'ec65db48f140320c9eca988b210dc8d6'
  priv_key = 'c7a359bcfc51c6440ba472e18225b359c314f149'
  
  def hash_params(self):
    hash_md5 = md5()
    hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()
    return hashed_params
  
  def get_heroes(self):
    params = {'ts':self.timestamp, 'apikey': self.pub_key, 'hash': self.hash_params()}
    results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)
    
    data = results.json()
    print(data)
    print(data['status'])

mv = RestMarvel()
mv.get_heroes()