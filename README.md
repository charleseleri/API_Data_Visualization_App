# API-Based Interactive Data Visualization App

## Overview
This project is an **interactive stock market visualization app** that fetches real-time stock price data from the **Yahoo Finance API** and displays it using **Matplotlib & Seaborn**. Users can enter a stock ticker (e.g., AAPL, TSLA) and instantly visualize price trends.

## Features
- **Fetches real-time stock data** via Yahoo Finance API
- **Displays stock price trends** using interactive line charts
- **User input support** for selecting different stocks
- **Python-based backend** with automated data processing

## Project Structure
```
API_Data_Visualization_App/
│-- README.md                 # Project Overview & Instructions
│-- app.py                    # API Fetching & Data Processing
│-- dashboard.py               # Interactive Visualization
│-- requirements.txt           # Dependencies
│-- stock_data.csv (optional)  # Sample dataset (generated on first run)
```

## Installation & Setup
### 1️⃣ Install Dependencies
Run the following command to install required Python libraries:
```
pip install -r requirements.txt
```

### 2️⃣ Run the App
**Step 1:** Fetch stock data by running:
```
python app.py
```
This will save stock data to `stock_data.csv`.

**Step 2:** Visualize stock price trends by running:
```
python dashboard.py
```
Enter a stock ticker (e.g., `AAPL`, `TSLA`, `MSFT`) when prompted to generate an interactive chart.

## Technologies Used
- **Python** (Pandas, Requests, Matplotlib, Seaborn)
- **Yahoo Finance API** (Stock Data)
- **Interactive Data Visualization**

## Author
**Charles Eleri**

## Next Steps
- Add **Flask or Streamlit** for web-based visualization
- Expand API support to **crypto & forex markets**
- Deploy the app for public use

---
🔹 **GitHub Repo:** [github.com/charleseleri](https://github.com/charleseleri)
