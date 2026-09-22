import yfinance as yf
import matplotlib.pyplot as plt


#function to fetch data from api
def fetch_data(stock_name):
    data = yf.Ticker(stock_name)
    return(data)

def data_type(stock_name):
    data = fetch_data(stock_name)

    print("Info:")
    print(f"Company Name: {data.info['longName']}")
    print(f"Quote Type: {data.info['quoteType']}")
    print(f"Market Cap: {data.info['marketCap']}")
    print(f"Sector: {data.info['sector']}")
    print(f"Business Summary: {data.info['longBusinessSummary']}")


    print("\nHistory:")
    print(data.history(period="1y"))


stock_name = input("Enter stock name: ")
data_type(stock_name)
# plot simple graph

