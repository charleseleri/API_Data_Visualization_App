import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app import fetch_stock_data

# Function to visualize stock data
def plot_stock_data(ticker):
    stock_data = fetch_stock_data(ticker)
    
    if stock_data is not None:
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=stock_data["Date"], y=stock_data["Closing Price"], marker="o", linestyle="-", color="b")
        plt.xlabel("Date")
        plt.ylabel("Closing Price ($)")
        plt.title(f"Stock Price Trend for {ticker}")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
    else:
        print("Error: Could not retrieve stock data.")

# Example Usage
if __name__ == "__main__":
    ticker = input("Enter a stock ticker (e.g., AAPL, TSLA, MSFT): ").upper()
    plot_stock_data(ticker)
