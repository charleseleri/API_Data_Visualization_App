import requests
import pandas as pd
import datetime

# Function to fetch stock market data from Yahoo Finance API
def fetch_stock_data(ticker, interval="1d", range_period="1mo"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval={interval}&range={range_period}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        timestamps = data["chart"]["result"][0]["timestamp"]
        prices = data["chart"]["result"][0]["indicators"]["quote"][0]["close"]
        
        # Convert timestamps to human-readable dates
        dates = [datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d') for ts in timestamps]
        
        # Create DataFrame
        df = pd.DataFrame({"Date": dates, "Closing Price": prices})
        return df
    else:
        print("Failed to fetch stock data.")
        return None

# Example usage
if __name__ == "__main__":
    ticker = "AAPL"  # Apple Inc. stock
    stock_data = fetch_stock_data(ticker)
    if stock_data is not None:
        print(stock_data.head())
        stock_data.to_csv("stock_data.csv", index=False)  # Save to CSV
