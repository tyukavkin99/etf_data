import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def get_clean_data(data_path, number_of_stocks):
    number_of_columns = number_of_stocks+2
    df = pd.read_excel(data_path, header=1)\
        .reset_index()\
        .iloc[1:,:]\
        .drop(columns=["Ticker"])\
        .rename(columns={"Unnamed: 1":"Date"})\
        .iloc[:,:number_of_columns]
    df_na = df.fillna(0)
    df_na["Date"] = pd.to_datetime(df_na["Date"])
    df_na = df_na.set_index("Date")
    return df_na

def get_number_of_stocks():
    with open("number_of_stocks.txt", "r") as f:
        number_of_stocks = f.readline()
        number_of_stocks = number_of_stocks.replace("\n", "")
        return int(number_of_stocks)

def get_line_plot(df):
    figure = px.line(data_frame=df)
    return figure

def main():
    st.set_page_config(layout="wide")
    st.header("Stock Data Analysis")
    number_of_stocks = get_number_of_stocks()
    df = get_clean_data("tickers.xlsx", number_of_stocks=number_of_stocks)
    fig = get_line_plot(df=df)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()