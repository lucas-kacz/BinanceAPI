import time
import json
import hmac
import hashlib
import requests
from urllib.parse import urljoin, urlencode

API_KEY = "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
SECRET_KEY = "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
BASE_URL = "https://api.binance.com"

headers = {
    'X-MBX-APIKEY': API_KEY
}


PATH='/api/v1/time'
params = None

class BinanceException(Exception):
    def __init__(self, status_code, data):

        self.status_code = status_code
        if data:
            self.code = data['code']
            self.msg = data['msg']
        else:
            self.code = None
            self.msg = None
        message = f"{status_code} [{self.code}] {self.msg}"

        # Python 2.x
        # super(BinanceException, self).__init__(message)
        super().__init__(message)


PATH =  '/api/v1/time'
params = None

timestamp = int(time.time() * 1000)

url = urljoin(BASE_URL, PATH)
r = requests.get(url, params=params)
if r.status_code == 200:
    # print(json.dumps(r.json(), indent=2))
    data = r.json()
    print(f"diff={timestamp - data['serverTime']}ms")
else:
    raise BinanceException(status_code=r.status_code, data=r.json())


# PATH = '/api/v3/exchangeInfo'

# url = urljoin(BASE_URL, PATH)
# r = requests.get(url, headers=headers, params=params)
# if r.status_code == 200:
#     t = r.json()
#     for d in t["symbols"] :
#         print(d["symbol"])

# else:
#     raise BinanceException(status_code=r.status_code, data=r.json())

def getDepth(direction, pair):
    PATH = '/api/v3/depth'

    params = {
        'symbol': pair
    }

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        t = r.json()
        for d in t[direction] :
            print(d)

    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

getDepth('bids', 'BTCUSDT')

# PATH = '/api/v3/depth'

# params = {
#     'symbol': 'BTCUSDT'
# }

# url = urljoin(BASE_URL, PATH)
# r = requests.get(url, headers=headers, params=params)
# if r.status_code == 200:
#     t = r.json()
#     print(t)
# else:
#     raise BinanceException(status_code=r.status_code, data=r.json())


