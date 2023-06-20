# The requests library is used to send HTTP requests in Python.
import requests
# The json library is used for parsing JSON strings and converting Python data structures to JSON format.
import json

# An API request is made using the requests library. The request is made to the CoinMarketCap API, with parameters to get the latest 5 cryptocurrencies, converted to USD.
api_req = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=YOUR_API_KEY")

# The json.loads() function is used to parse the JSON content from the API response.
api = json.loads(api_req.content)

# Printing the symbol of the first cryptocurrency in the list.
print(api["data"][0]["symbol"])

# Printing the price of the first cryptocurrency, formatted to two decimal places.
print("{0:.2f}".format(api["data"][0]["quote"]["USD"]["price"]))

# Defining a list of coins that you own, with details such as the symbol of the coin, the amount you own, and the price you paid per coin.
coins = [
            {
                "symbol": "BTC",
                "amount_owned": 2,
                "price_per_coin": 19300.00
            },
            {
                "symbol": "ETH",
                "amount_owned": 7,
                "price_per_coin": 519.00
            },
         ]

# Initializing the total profit/loss variable.
total_pl = 0

# Looping through the first 5 cryptocurrencies in the API response.
for i in range(0,5):
    # Looping through your list of owned coins.
    for coin in coins:
        # If the symbol of the current cryptocurrency from the API matches the symbol of your owned coin, then we calculate the profit/loss.
        if api["data"][i]["symbol"] == coin["symbol"]:
            # Total amount paid for the coin is calculated.
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            # Current value of the coin is calculated.
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            # Profit/loss per coin is calculated.
            pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            # Total profit/loss for this coin is calculated.
            total_pl_coin = pl_per_coin * coin["amount_owned"]

            # Total profit/loss for all coins is updated.
            total_pl = total_pl + total_pl_coin

            # Print the details for the coin.
            print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
            print("Price - {0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("Number of Coin:", coin["amount_owned"])
            print("Total amount paid - {0:.2f}".format(total_paid))
            print("Current value - {0:.2f}".format(current_value))
            print("P/L per coin - {0:.2f}".format(pl_per_coin))
            print("-------------------------------")

# Print the total profit/loss for the entire portfolio.
print("Total P/L For total Portfolio - {0:.2f}".format(total_pl))

# This script helps users track the profit or loss of their cryptocurrency investments.
# It provides a high-level snapshot of the performance of the user's portfolio, based on the latest market prices.
# It first fetches the top 5 latest cryptocurrencies from the CoinMarketCap API, then it goes through the user's portfolio (defined in the 'coins' list)
# to see if the user has any of these top cryptocurrencies. If a match is found, it calculates the current market value of the user's holding in that cryptocurrency
# as well as the profit or loss since the user's investment.
# Finally, it adds up all the profits and losses across all cryptocurrencies in the user's portfolio to present the total profit or loss.
# This tool is useful for users to stay informed about their cryptocurrency investments and make informed decisions based on the latest market data.
