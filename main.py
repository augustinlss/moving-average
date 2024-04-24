import utils.data
import utils.strategy 

def main():
    # Input parameters
    ticker = 'AAPL'  # Example ticker symbol (Apple Inc.)
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    short_window = 20  # Short-term moving average window
    long_window = 50   # Long-term moving average window

    DataHandler = utils.data.DataHandler
    MovingAverage = utils.strategy.MovingAverage
    # Fetch stock data
    stock_data = DataHandler.fetchData(ticker, start_date, end_date)

    # Calculate moving averages
    short_ma = MovingAverage.calculate_moving_average(stock_data, short_window)
    long_ma = MovingAverage.calculate_moving_average(stock_data, long_window)

    # Print signals
    print(signals)
    # Plot data with moving averages
    DataHandler.plotMovingAverage(stock_data, short_ma, ticker)

    # Implement trading strategy
    signals = MovingAverage.implement_trading_strategy(stock_data, short_ma, long_ma)

    
    
if __name__ == "__main__":
    main()