import time
import json
import hmac
import hashlib
import requests
import os
import sqlite3
from sqlite3 import Error
from urllib.parse import urljoin, urlencode

API_KEY = ""
SECRET_KEY = ""
BASE_URL = "https://api.binance.com"

database_path = "C:/Users/Lucas Kaczmarski/OneDrive - De Vinci/Documents/Esilv/A4/SqLite Databases/td9.db"

headers = {
    'X-MBX-APIKEY': API_KEY
}

con = sqlite3.connect(os.path.abspath(database_path))
cur = con.cursor()

for row in cur.execute('''SELECT * FROM my_table'''):
    print(row)


# def create_connection(database_path):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(database_path) 
#     except Error as e:
#         print(e)

#     return conn


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


def all_assets():
    PATH = '/api/v3/exchangeInfo'

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        t = r.json()
        for d in t["symbols"] :
            print(d["symbol"])

    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

#all_assets()

def getDepth(direction, pair):
    PATH = '/api/v3/depth'

    params = {
        'symbol': pair
    }

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        t = r.json()
        # for d in t[direction] :
        #     print(type(t[direction]))
        #     # print(d[0])
        #     # print(type(d[0]))
        print(t[direction][0])

    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

getDepth('asks', 'BTCUSDT')

def orderBook(pair):
    PATH = '/api/v3/depth'

    params = {
        'symbol': pair
    }

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        t = r.json()
        print(t)
        # for d in t[direction] :
        #     print(type(t[direction]))
        #     # print(d[0])
        #     # print(type(d[0]))


    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

#orderBook('BTCUSDT')


def getCandle(pair, interval):
    PATH = '/api/v3/uiKlines'

    params = {
        'symbol': pair,
        'interval': interval
    }

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        t = r.json()
        print(t)
        # for d in t[direction] :
        #     print(type(t[direction]))
        #     # print(d[0])
        #     # print(type(d[0]))
        date = t[0][0]
        high = t[0][2]
        low = t[0][3]
        open = t[0][1]
        close = t[0][4]
        volume = t[0][5]

        print(f'''{date}''')

        sql = f'''INSERT INTO my_table(
            {date}, 
            {high}, 
            {low}, 
            {open}, 
            {close}, 
            {volume}
            );'''
        cur.execute(f"""INSERT INTO my_table(date,high,low,open,close,volume)
            VALUES(
            {date}, 
            {high}, 
            {low}, 
            {open}, 
            {close}, 
            {volume}
            );""")
        con.commit()

    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

#getCandle('BTCUSDT', '5m')

def exchangeInfo(pair):
    PATH = 'api/v3/exchangeInfo'

    params = {
        'symbol': pair
    }

    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        t = r.json()
        #print(t)
        selection1 = t.get('symbols')
        selection2=selection1[0].get('filters')
        print(selection2)
        minNotional = selection2[2].get('minNotional')
        minAndMaxPrice = selection2[6]
        print('La valeur minimale a acheter est de ' + minNotional + ' tokens')
        print('Les multiplicateurs des prix pour les achats et ventes sont les suivants :')
        print(minAndMaxPrice)
        return minNotional

    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

exchangeInfo('BTCUSDT')

def createOrder(api_key, secret_key, direction, price, pair, orderType):
    PATH = 'api/v3/order'
    timestamp = int(time.time() * 1000)

    params = {
        'symbol': pair,
        'side': direction,
        'type': orderType,
        'timeInForce': 'GTC',
        'quantity': exchangeInfo(pair),
        'price': price,
        'recvWindow': 5000,
        'timestamp': timestamp
    }

    query_string = urlencode(params)
    params['signature'] = hmac.new(secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())


createOrder(API_KEY, SECRET_KEY, "BUY", 16000, "BTCUSDT", "LIMIT")

def cancelOrder(api_key, secret_key, pair, uuid):
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)

    params = {
        'symbol' : pair,
        'orderId' : uuid,
        'timestamp' : timestamp
    }

    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, PATH)
    r = requests.delete(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data, indent=2))
    else:
        raise BinanceException(status_code=r.status_code, data=r.json())

#cancelOrder(API_KEY, SECRET_KEY, 'BTCUSDT', )