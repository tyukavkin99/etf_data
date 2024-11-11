import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from components.get_symbols import DataIngestion
from components.get_stock_data import DataFrameStock
import sys
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from openpyxl.workbook import Workbook

def get_dates():
    ''' Returns the current date and date 2 years ago '''
    current = date.today()
    past_date = current - relativedelta(years=2)
    current, past_date = current.strftime("%Y-%m-%d"), past_date.strftime("%Y-%m-%d")
    return current, past_date

def main():
    '''Outputs requested stock data and number of stocks'''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    url = "https://finance.yahoo.com/u/yahoo-finance/watchlists/semiconductor-stocks/" 	
    symbol_list = DataIngestion(url, headers).get_data()
    current, past_date = get_dates()
    stock_getter = DataFrameStock(symbol_list, current_date=current, past_date=past_date)
    number_of_stocks = stock_getter.get_number_of_stocks()
    df = stock_getter\
        .get_dataframe()\
        .reset_index()
    df['Date'] = df['Date'].dt.tz_localize(None)
    df.to_excel("data/tickers.xlsx")
    with open("data/number_of_stocks.txt", "w+") as f:
        f.write(str(number_of_stocks))


if __name__ == "__main__":
    main()
