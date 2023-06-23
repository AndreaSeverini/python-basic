from tkinter import *

# The requests library is used to send HTTP requests in Python.
import requests
# The json library is used for parsing JSON strings and converting Python data structures to JSON format.
import json

print("||||||||||||||||||||||||||||||||")


# This function will be used to change the font color based on the value of 'amount'.


def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


# This function will make a request to the CoinMarketCap API to get the latest prices for cryptocurrencies.
# It then calculates the profit or loss for each coin in your portfolio and displays this information in the GUI.


def my_portfolio():
    # Make a request to the CoinMarketCap API.
    api_req = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/"
                           "listings/latest?start=1&limit=5&"
                           "convert=USD&CMC_PRO_API_KEY=YOUR_API_KEY")

    # The json.loads() function is used to parse the JSON content from the API response.
    api = json.loads(api_req.content)

    # Printing the symbol of the first cryptocurrency in the list.
    print(api["data"][0]["symbol"])

    # Printing the price of the first cryptocurrency, formatted to two decimal places.
    print("{0:.2f}".format(api["data"][0]["quote"]["USD"]["price"]))

    # Defining a list of coins that you own, with details such as the symbol of the coin,
    # the amount you own, and the price you paid per coin.
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
    total_pl = 0.0
    coin_row = 1
    total_current_value = 0
    current_value = 0

    # Looping through the first 5 cryptocurrencies in the API response.
    for i in range(0, 5):
        # Looping through your list of owned coins.
        for coin in coins:
            # If the symbol of the current cryptocurrency from the API
            # matches the symbol of your owned coin, then we calculate the profit/loss.
            if api["data"][i]["symbol"] == coin["symbol"]:
                # Total amount paid for the coin is calculated.
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                # Current value of the coin is calculated.
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                # Profit/loss per coin is calculated.
                pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                # Total profit/loss for this coin is calculated.
                total_pl_coin = pl_per_coin * float(coin["amount_owned"])
                total_current_value = total_current_value + current_value

                # Total profit/loss for all coins is updated.
                total_pl = total_pl + total_pl_coin

                # Print the details for the coin.
                print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                print("Number of Coin:", coin["amount_owned"])
                print("Total amount paid - ${0:.2f}".format(total_paid))
                print("Current value - ${0:.2f}".format(current_value))
                print("P/L per coin - ${0:.2f}".format(pl_per_coin))
                print("-------------------------------")

                name = Label(portfolio_app, text=api["data"][i]["symbol"], fg="black", bg="white", font="Lato 12 bold",
                             padx="3", pady="3", borderwidth=1)
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(portfolio_app, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),
                              fg="black", bg="white", font="Lato 12 bold", padx="3", pady="3", borderwidth=1)
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                no_coins = Label(portfolio_app, text=coin["amount_owned"], fg="black", bg="white", font="Lato 12 bold",
                                 padx="3", pady="3", borderwidth=1)
                no_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(portfolio_app, text="${0:.2f}".format(total_paid), fg="black", bg="white",
                                    font="Lato 12 bold", padx="3", pady="3", borderwidth=1)
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_val = Label(portfolio_app, text="${0:.2f}".format(current_value), fg="black", bg="white",
                                    font="Lato 12 bold", padx="3", pady="3", borderwidth=1)
                current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_coin = Label(portfolio_app, text="${0:.2f}".format(pl_per_coin),
                                fg=font_color(float("{0:.2f}".format(current_value))), bg="white", font="Lato 12 bold",
                                padx="3", pady="3", borderwidth=1)
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                total_prof_loss = Label(portfolio_app, text="${0:.2f}".format(total_pl),
                                        fg=font_color(float("{0:.2f}".format(current_value))), bg="white",
                                        font="Lato 12 bold", padx="3", pady="3", borderwidth=1)
                total_prof_loss.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row = coin_row + 1

    api = ""  # empty the api variable
    # Print the total profit/loss for the entire portfolio.
    print("Total P/L For total Portfolio - ${0:.2f}".format(total_pl))

    total_current = Label(portfolio_app, text="${0:.2f}".format(total_current_value),
                          fg=font_color(float("{0:.2f}".format(current_value))), bg="white",
                          font="Lato 12 bold", padx="3", pady="3", borderwidth=1)
    total_current.grid(row=coin_row, column=4, sticky=N + S + E + W)
    total_portfolio_prof_loss = Label(portfolio_app, text="${0:.2f}".format(total_pl),
                                      fg=font_color(float("{0:.2f}".format(current_value))), bg="white",
                                      font="Lato 12 bold", padx="3", pady="3", borderwidth=1)
    total_portfolio_prof_loss.grid(row=coin_row, column=6, sticky=N + S + E + W)

    update = Button(portfolio_app, command=my_portfolio, text="Update", fg="white", bg="black",
                    font="Lato 16 bold", padx="5", pady="5", borderwidth=2)
    update.grid(row=coin_row + 1, column=6, sticky=N + S + E + W)


# 1 Create an instance with Tk() Class


portfolio_app = Tk()
portfolio_app.title("My Portfolio App")
# portfolio_app.iconbitmap('favicon.ico')

name_header = Label(portfolio_app, text="Coin Name", bg="black", fg="white",
                    font="Lato 12 bold", padx="8", pady="8", borderwidth=3)
name_header.grid(row=0, column=0, sticky=N + S + E + W)

price_header = Label(portfolio_app, text="Price", bg="black", fg="white",
                     font="Lato 12 bold", padx="8", pady="8", borderwidth=3)
price_header.grid(row=0, column=1, sticky=N + S + E + W)

no_coins_header = Label(portfolio_app, text="Coin Owned", bg="black", fg="white",
                        font="Lato 12 bold", padx="8", pady="8", borderwidth=3)
no_coins_header.grid(row=0, column=2, sticky=N + S + E + W)

amount_paid_header = Label(portfolio_app, text="Total Amount Paid", bg="black", fg="white",
                           font="Lato 12 bold", padx="8", pady="8", borderwidth=3)
amount_paid_header.grid(row=0, column=3, sticky=N + S + E + W)

current_val_header = Label(portfolio_app, text="Current Value", bg="black", fg="white",
                           font="Lato 12 bold", padx="8", pady="8", borderwidth=3)
current_val_header.grid(row=0, column=4, sticky=N + S + E + W)

pl_coin_header = Label(portfolio_app, text="P/L per coin", bg="black", fg="white",
                       font="Lato 12 bold", padx="8", pady="8", borderwidth=3)
pl_coin_header.grid(row=0, column=5, sticky=N + S + E + W)

# Here, you're creating a new label widget (which is like a piece of text) in your application window ('portfolio_app').
# The text of this label is "Total P/L with coin".
# The font is set to 'Lato' with size 12 and in bold.
# Padding is added around the label text with 'padx' and 'pady'.
# A border is added around the label with a thickness of 3 pixels.

total_pl_header = Label(portfolio_app, text="Total P/L with coin", bg="black", fg="white", font="Lato 12 bold", padx="8", pady="8", borderwidth=3)

# The 'grid' method is used to place the label in the application window.
# The 'row' and 'column' parameters specify the position of the label in the window grid.
# The 'sticky' parameter is used to specify which sides of the cell the widget should stick to.
total_pl_header.grid(row=0, column=6, sticky=N + S + E + W)

# At this point, you're calling the 'my_portfolio' function which you defined earlier.
# This function makes a request to the CoinMarketCap API and updates your portfolio in the GUI.
my_portfolio()

# The 'mainloop' function is called to start the Tkinter event loop.
# The event loop is an infinite loop where the program waits for user events such as button clicks or key presses.
portfolio_app.mainloop()

# This print statement is used to print a line of '|' characters in the console for visual separation.
print("||||||||||||||||||||||||||||||||")

# You're mentioning a command to install the 'pyinstaller' package using pip.
# 'pyinstaller' is a package that freezes (packages) Python applications into stand-alone executables.
# These executables can be run on the systems even if Python is not installed on them.

# You're reminding to use your api key and substitute it in the REST API endpoint searchParams

# The command 'pyinstaller --windowed --name=MyApp main.py' is a command that
# can be run in the terminal to package your Python script into an executable.
# The '--windowed' option is used to specify that the executable should be a GUI application, not a console application.
# The '--name' option is used to specify the name of the executable.

# You're reminding to execute the app. After running the pyinstaller command,
# an executable file will be created which can be run to start the application.
