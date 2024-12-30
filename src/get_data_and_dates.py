import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.get_symbols import DataIngestion
from src.get_stock_data import DataFrameStock
import sys
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from openpyxl.workbook import Workbook

class GetDataDates:
    
    def get_dates():
        ''' Returns the current date and date 2 years ago '''
        current = date.today()
        past_date = current - relativedelta(years=2)
        current, past_date = current.strftime("%Y-%m-%d"), past_date.strftime("%Y-%m-%d")
        return current, past_date

    def get_data():
        '''Outputs requested stock data and number of stocks'''
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
        url = "https://finance.yahoo.com/u/motif/watchlists/semiconductor-stocks/" 	
        symbol_list = DataIngestion.get_data(url, headers)
        current, past_date = GetDataDates.get_dates()
        stock_getter = DataFrameStock(symbol_list, current_date=current, past_date=past_date)
        stock_getter.set_number_of_stocks()
        n_of_stocks = stock_getter.number_of_stocks
        print("Stock data: ", stock_getter.stocks)        
        print("Current date: ", stock_getter.current_date)
        print("Past data: ", stock_getter.past_date)        
        df = stock_getter\
            .get_dataframe()\
            .reset_index()
        df['Date'] = df['Date'].dt.tz_localize(None)
        df.to_excel("data/tickers.xlsx")
        print("New dataset was added")
        with open("data/number_of_stocks.txt", "w+") as f:
            f.write(str(n_of_stocks))
        print("Number of stocks was added")