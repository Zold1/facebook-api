import hashlib
import random
import requests
import urllib.parse as urlparse
from urllib.parse import urlencode

class facebook:
  ACCESS_TOKEN = ''
  EMAIL = ''
  PASSWORD = ''

  def data(self):
    api_key = '882a8490361da98702bf97a021ddc14d'
    api_secret = '62f8ce9f74b12f84c123cc23437a4a32'
    data = {
      'api_key': api_key,
      'credentials_type': 'password',
      'email': self.EMAIL,
      'format': 'JSON',
      'generate_machine_id': '1',
      'generate_session_cookies': '1',
      'locale': 'en_US',
      'method': 'auth.login',
      'password': self.PASSWORD,
      'return_ssl_resources': '0',
      'v': '1.0'
    }
    sig = ''
    for key, value in data.items():
      sig += key+"="+value
    sig += api_secret
    sig = hashlib.md5(sig.encode('utf-8')).hexdigest() 
    data['sig'] = sig
    return data

  def url_configure(self, url, params):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)

  def access_token(self, email, password): # Get android full access token
    base_url = 'https://api.facebook.com/restserver.php'
    self.EMAIL = email
    self.PASSWORD = password
    
    useragents = [
      'Mozilla/5.0 (Linux; Android 5.0.2; Andromax C46B2G Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/60.0.0.16.76;]',
      '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]',
      'Mozilla/5.0 (Linux; Android 5.1.1; SM-N9208 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36',
      'Mozilla/5.0 (Linux; U; Android 5.0; en-US; ASUS_Z008 Build/LRX21V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.8.0.718 U3/0.8.0 Mobile Safari/534.30',
      'Mozilla/5.0 (Linux; U; Android 5.1; en-US; E5563 Build/29.1.B.0.101) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30',
      'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; Celkon A406 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    ]
    useragent = random.choice(useragents)
    headers = {
      'User-Agent': useragent
    }
    url_parts = list(urlparse.urlparse(base_url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(self.data())
    url_parts[4] = urlencode(query)
    response = requests.get(urlparse.urlunparse(url_parts), headers=headers).json()
    try:
      response['access_token']
    except:
      return response
    else:
      self.ACCESS_TOKEN = response['access_token']
      return self.ACCESS_TOKEN

  def set_access_token(self, access_token):
    self.ACCESS_TOKEN = access_token
  
  def graph(self, method, object, object_id, params = {}):
    graph = 'https://graph.facebook.com/'
    fixed_data = {
      'method': method,
      'access_token': self.ACCESS_TOKEN
    }
    data = {**fixed_data, **params}
    url = self.url_configure(graph+str(object_id)+'/'+object, data)
    return requests.get(url).json()