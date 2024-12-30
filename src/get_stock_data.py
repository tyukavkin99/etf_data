import pandas as pd
import numpy as np
import yfinance as yf

class DataFrameStock():
	def __init__(self, stocks, current_date=None, past_date=None):
		self.stocks = stocks
		self._current_date = current_date
		self._past_date = past_date
		self._number_of_stocks = None
	
	@property	
	def current_date(self):
		return self._current_date
	
	@property
	def past_date(self):
		return self._past_date

	@current_date.setter
	def current_date(self, value):
		self._current_date = value
	
	@past_date.setter
	def past_date(self, value):
		self._past_date = value
	
	def get_dataframe(self):
		df = yf.download(self.stocks, start=self.past_date, end=self.current_date, interval="1wk", auto_adjust=True)
		return df

	@property	
	def number_of_stocks(self):
		return self._number_of_stocks

	def set_number_of_stocks(self):
		self._number_of_stocks = len(self.stocks)
'''
if __name__ == "__main__":
	test1 = DataFrameStock(["NVDA"], 2024-12-30, 2022-12-30) '''
