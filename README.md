
# 📊 Tesla Stock Forecast Dashboard

This project is a Streamlit-based interactive dashboard for forecasting Tesla stock prices using classical and deep learning models.

## 🚀 Features

- 📈 Time Series Forecasting using:
  - ARIMA
  - SARIMA
  - LSTM
  - GRU
- 📊 Model comparison with RMSE, MAE, MSE
- 📉 Interactive plots for actual vs predicted prices
- 🔍 Clean UI built with Streamlit

## 📂 Files Used
- `tesla_stock.csv`: Historical Tesla stock prices
- `tesla_forecast_comparison_final.csv`: ARIMA/SARIMA forecasts
- `deep_learning_forecast.csv`: LSTM/GRU predictions
- `app.py`: Streamlit app script
- `requirements.txt`: Python dependency list

## 📽 Demo Preview
🎥 https://drive.google.com/file/d/1853sigCVOq5Ys1WVq-gcKjvM2YchQslb/view?usp=sharing

## 📌 How to Run Locally

```bash
git clone https://github.com/Akashanjalo/tesla-stock-dashboard.git
cd tesla-stock-dashboard
pip install -r requirements.txt
streamlit run app.py
