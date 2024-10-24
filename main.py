import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_symbols import DataIngestion
from get_stock_data import DataFrameStock
import sys
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from openpyxl.workbook import Workbook

def get_dates():
    current = date.today()
    past_date = current - relativedelta(years=2)
    current, past_date = current.strftime("%Y-%m-%d"), past_date.strftime("%Y-%m-%d")
    return current, past_date

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    url = "https://finance.yahoo.com/u/yahoo-finance/watchlists/semiconductor-stocks/" 	
    symbol_list = DataIngestion(url, headers).get_data()
    current, past_date = get_dates()
    df, number_of_stocks = DataFrameStock(symbol_list, current_date=current, past_date=past_date)
    df = df\
        .get_dataframe()\
        .reset_index()
    df['Date'] = df['Date'].dt.tz_localize(None)
    df.to_excel("tickers.xlsx")
    with open("number_of_stocks.txt", "w+") as f:
        f.write(str(number_of_stocks))


if __name__ == "__main__":
    main()
