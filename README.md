# BinanceAPI

The purpose of this project is to learn to use crypto exchanges APIs using Python 3 or Javascript. In our case we use Python. For our project we use the Binance API.

## How to run

In order to test the project yourself, you need to clone the repo and then enter your Binance API_KEY and SECRET_KEY.

## Functions

`all_assets()` : Returns all the pairs listed on Binance

`getDepth(direction, pair)` : Returns the first ask or bid price of an asset

`orderBook(pair)` : Returns the whole order book for the given pair

`getCandle(pair, interval)` : Returns the candle for a given pair and interval (date, high, low, open, close, volume)

`exchangeInfo(pair)` : -Returns the min quantity of tokens a user can buy in this pair
                       -Returns the multipliers of prices the user can input when creating an order. For example, for the BTCUST pair, the bidMultiplierUp is 5 and bidMultiplierDown is 0.2. If the actual price is 16.000$ the given price must be between 16.000*0.2 <= your_price <= 16.000*5.
