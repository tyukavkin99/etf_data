import pandas as pd


df = pd.read_html("https://www.etf.com/topics/semiconductors")

print(df)