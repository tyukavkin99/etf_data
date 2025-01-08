import pandas as pd
import numpy as np

def get_returns(df: pd.DataFrame) -> pd.DataFrame:
	return df.pct_change().fillna(0)

def get_average_returns(df: pd.DataFrame) -> pd.DataFrame:
	return df.mean()

def get_std_returns(df: pd.DataFrame) -> pd.DataFrame:
	return df.std()

def get_moving_averages(df: pd.DataFrame, window_size) -> pd.DataFrame:
	return df.rolling(window=window_size).mean()
