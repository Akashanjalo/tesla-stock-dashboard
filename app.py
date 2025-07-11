# -*- coding: utf-8 -*-
"""App.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qYWaq4Fe87lDuFEYKnZL3fFZgpTdpTUP
"""

# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

st.set_page_config(page_title="Tesla Forecast Dashboard", layout="wide")

st.title("📈 Tesla Stock Forecast Dashboard")
st.markdown("Developed by **Akash Anjalo** — ARIMA | SARIMA | LSTM | GRU")

# ------------------------------
# 🔃 Load Data
@st.cache_data
def load_data():
    stock = pd.read_csv("tesla_stock.csv", skiprows=2)
    stock.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
    stock["Date"] = pd.to_datetime(stock["Date"])
    stock.set_index("Date", inplace=True)

    forecast = pd.read_csv("tesla_forecast_comparison_final.csv")
    forecast["Date"] = pd.to_datetime(forecast["Date"])
    forecast.set_index("Date", inplace=True)

    deep = pd.read_csv("deep_learning_forecast.csv")
    deep["Date"] = pd.to_datetime(deep["Date"])
    deep.set_index("Date", inplace=True)

    return stock, forecast, deep

df, forecast_df, deep_df = load_data()

# ------------------------------
# 📊 Sidebar Controls
st.sidebar.header("View Options")
show_ma = st.sidebar.checkbox("Show Moving Averages", value=True)
show_forecast = st.sidebar.checkbox("Show ARIMA vs SARIMA Forecast", value=True)
show_dl = st.sidebar.checkbox("Show LSTM & GRU Forecast", value=True)
show_table = st.sidebar.checkbox("Show Forecast Tables", value=False)

# ------------------------------
# 📈 Tesla Close Price Chart
st.subheader("📉 Tesla Close Price with Moving Averages")
fig, ax = plt.subplots(figsize=(12, 5))
df["Close"].plot(ax=ax, label="Close", alpha=0.7)

if show_ma:
    df["MA7"] = df["Close"].rolling(7).mean()
    df["MA30"] = df["Close"].rolling(30).mean()
    df["MA7"].plot(ax=ax, label="7-Day MA")
    df["MA30"].plot(ax=ax, label="30-Day MA")

ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.set_title("Tesla Close Price")
ax.legend()
ax.grid()
st.pyplot(fig)

# ------------------------------
# 🔮 ARIMA vs SARIMA Forecast
if show_forecast:
    st.subheader("🔮 ARIMA vs SARIMA Forecast")
    fig2, ax2 = plt.subplots(figsize=(12, 5))
    forecast_df["Actual"].plot(ax=ax2, label="Actual", color="black")
    forecast_df["ARIMA_Forecast"].plot(ax=ax2, label="ARIMA", linestyle="--", color="blue")
    forecast_df["SARIMA_Forecast"].plot(ax=ax2, label="SARIMA", linestyle="--", color="red")
    ax2.set_title("ARIMA & SARIMA Forecast")
    ax2.legend()
    ax2.grid()
    st.pyplot(fig2)

# ------------------------------
# 🤖 LSTM vs GRU Forecast
if show_dl:
    st.subheader("🤖 LSTM vs GRU Forecast")
    fig3, ax3 = plt.subplots(figsize=(12, 5))
    deep_df["Actual"].plot(ax=ax3, label="Actual", color="black")
    deep_df["LSTM_Pred"].plot(ax=ax3, label="LSTM Forecast", linestyle="--", color="green")
    deep_df["GRU_Pred"].plot(ax=ax3, label="GRU Forecast", linestyle="--", color="purple")
    ax3.set_title("LSTM & GRU Forecast")
    ax3.legend()
    ax3.grid()
    st.pyplot(fig3)

# ------------------------------
# 📋 Show Data Tables
if show_table:
    st.subheader("🧾 Forecast Data Table – ARIMA & SARIMA")
    st.dataframe(forecast_df.round(2))

    st.subheader("🧠 Forecast Data Table – LSTM & GRU")
    st.dataframe(deep_df.round(2))

# ------------------------------
# 📊 Metrics Comparison Table
def compute_metrics(true, pred):
    mse = mean_squared_error(true, pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(true, pred)
    return round(mse, 2), round(rmse, 2), round(mae, 2)

st.subheader("📊 Model Performance Metrics")
metrics = {
    "ARIMA": compute_metrics(forecast_df["Actual"], forecast_df["ARIMA_Forecast"]),
    "SARIMA": compute_metrics(forecast_df["Actual"], forecast_df["SARIMA_Forecast"]),
    "LSTM": compute_metrics(deep_df["Actual"], deep_df["LSTM_Pred"]),
    "GRU": compute_metrics(deep_df["Actual"], deep_df["GRU_Pred"])
}

metric_df = pd.DataFrame(metrics, index=["MSE", "RMSE", "MAE"]).T
st.dataframe(metric_df)

# ------------------------------
st.markdown("---")
st.markdown("📌 Project Complete — Developed using Streamlit, StatsModels, TensorFlow, and Scikit-learn.")