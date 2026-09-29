import yfinance as yf
import matplotlib.pyplot as plt


#function to fetch ticker object from yahoo finance
def fetch_ticker(stock_name):
    data = yf.Ticker(stock_name)
    return(data)

def stock_info(stock_name):
    ticker = fetch_ticker(stock_name)

    print("Info:")
    print(f"Company Name: {ticker.info['longName']}")
    print(f"Quote Type: {ticker.info['quoteType']}")
    print(f"Market Cap: {ticker.info['marketCap']}")
    print(f"Sector: {ticker.info['sector']}")
    print(f"Business Summary: {ticker.info['longBusinessSummary']}")

    return(ticker.info)

def stock_history(stock_name):
    ticker = fetch_ticker(stock_name)
    history = ticker.history(period="1y")
    return(history)

stock_name = input("Enter stock name: ").upper()
info = stock_info(stock_name)
history = stock_history(stock_name)

# plot simple graph
print(history)
high_prices = history['High']
low_prices = history['Low']

average_price = (high_prices + low_prices) / 2
print(f"Average Price: {average_price}")

plt.plot(average_price)
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.title(info['longName'])
plt.show()

