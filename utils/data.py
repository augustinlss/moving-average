import yfinance as yf
import matplotlib.pyplot as plt

class DataHandler:
    def fetchData(ticker, startDate, endDate):
        stock_data = yf.download(ticker, start=startDate, end=endDate)
        return stock_data
    
    def plotMovingAverage(data, moving_average, ticker):
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Close'], label=ticker)
        plt.plot(moving_average.index, moving_average, label='Moving Average', color='red')
        plt.title(f'{ticker} Stock Price with Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()