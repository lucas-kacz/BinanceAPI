# BinanceAPI

The purpose of this project is to learn to use crypto exchanges APIs using Python 3 or Javascript. In our case we use Python. For our project we use the Binance API.

## How to run

In order to test the project yourself, you need to clone the repo and then enter your Binance API_KEY and SECRET_KEY.

## Functions

`all_assets()` : Returns all the pairs listed on Binance

`getDepth(direction, pair)` : Returns the first ask or bid price of an asset

`orderBook(pair)` : Returns the whole order book for the given pair

`getCandle(pair, interval)` : Returns the candle for a given pair and interval (date, high, low, open, close, volume). This functions fills and Sqlite3 table locally. ![SQLite3 Table](https://user-images.githubusercontent.com/113424948/209863221-1c7de99a-1913-4222-96f9-9a25f7e8f4c9.PNG)


`exchangeInfo(pair)` : 
* Returns the min quantity of tokens a user can buy in this pair
* Returns the multipliers of prices the user can input when creating an order. For example, for the BTCUST pair, the bidMultiplierUp is 5 and bidMultiplierDown is 0.2. If the actual price is 16.000$ the given price must be between 16.000 . 0.2 <= your_price <= 16.000 . 5.

`createOrder(api_key, secret_key, direction, price, pair, orderType)` : Creates an order if possible given the parameters. The user must respect the conditions of the `exchangeInfo(pair)` function.

`cancelOrder(api_key, secret_key, pair, uuid)` : Cancels an already created order given the Id and the pair.
