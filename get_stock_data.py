import pandas as pd
import numpy as np
import yfinance as yf

class DataFrameStock():
	def __init__(self, stocks, current_date=None, past_date=None):
		self.stocks = stocks
		self.current_date = current_date
		self.past_date = past_date
	
	def set_current_date(self, value):
		self.current_date = value
	
	def set_past_date(self, value):
		self.past_date = value
	
	def get_current_date(self):
		print(self.current_date)

	def get_past_date(self):
		print(self.past_date)

	def get_dataframe(self):
		df = yf.download(self.stocks, start=self.past_date, end=self.current_date, interval="1wk", auto_adjust=True)
		number_of_stocks = len(self.stocks)
		return df, number_of_stocks


