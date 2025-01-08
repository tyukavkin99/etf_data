import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import src.get_data_and_dates as get_excel_data
import src as fin_opt

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
    df_na = df_na.drop(columns="index")
    return df_na

def get_number_of_stocks():
    with open("data/number_of_stocks.txt", "r") as f:
        number_of_stocks = f.readline()
        number_of_stocks = number_of_stocks.replace("\n", "")
        return int(number_of_stocks)

def get_line_plot(df):
    figure = px.line(data_frame=df)
    return figure

def main():
    # Run script to get excel file
    get_excel_data.GetDataDates.get_data()

    # Page config
    st.set_page_config(layout="wide")

    # Header
    st.header("Stock Data Analysis of semiconductor companies")

    # Get Number of stocks
    number_of_stocks = get_number_of_stocks()

    # Get clean data
    df = get_clean_data("data/tickers.xlsx", number_of_stocks=number_of_stocks)

    # Get line plot for original data
    fig = get_line_plot(df=df)
    st.plotly_chart(fig, use_container_width=True)

    # Get returns
    returns_df = fin_opt.get_returns(df=df)
    st.write(returns_df)

    # Get line plot for returns
    fig2 = get_line_plot(df=returns_df)
    st.plotly_chart(fig2, use_container_width=True)

    # Get average returns
    avg_returns = fin_opt.get_average_returns(returns_df)
    st.write(avg_returns.to_frame().T)
    st.caption("This is average returns")

    # Get standard devidation of returns
    std_returns = fin_opt.get_std_returns(returns_df)
    st.write(std_returns.to_frame().T)
    st.caption("This is standard deviation of returns")

    # Get moving average
    moving_averages = fin_opt.get_moving_averages(returns_df, 3)
    fig3 = get_line_plot(moving_averages)
    st.plotly_chart(fig3)

if __name__ == "__main__":
    main()
