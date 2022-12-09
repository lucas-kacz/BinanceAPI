from binance.client import Client

api_key="vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
api_secret="NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"

client=Client(api_key, api_secret)

info = client.get_exchange_info()
print(info)

# info = client.get_margin_symbol(symbol='BTCUSDT')
# print(info)

# depth = client.get_order_book(symbol='ETHUSDT')
# print(depth)

tickers = client.get_orderbook_tickers()

#Question 2 : Ask for the bid price or ask price of a Pair listed on Binance
# def getDepth(direction, symbol):
#     for i in range (len(tickers)):
#         if tickers[i].get('symbol') == symbol :
#             print(tickers[i].get(direction))

# getDepth("bidPrice", "ETHUSDT")

# #Question 3 : Get the order book of an asset
# def display_order_book(pair):
#     print(client.get_order_book(symbol=pair))

# display_order_book("ETHBTC")

#Question 4 : Create a function to read aggregated trading data (candles)
# def refreshDataCandle(pair, duration):

# candles = client.get_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_30MINUTE)
# print(candles)







