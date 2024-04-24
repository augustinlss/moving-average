import pandas as pd

class MovingAverage:
    def calculate_moving_average(data, window):
        return data['Close'].rolling(window=window).mean()
    
    def implement_trading_strategy(data, moving_average_short, moving_average_long):
        signals = pd.DataFrame(index=data.index)
        signals['Price'] = data['Close']
        signals['Short_MA'] = moving_average_short
        signals['Long_MA'] = moving_average_long
        signals['Signal'] = 0.0
        signals['Signal'][moving_average_short > moving_average_long] = 1.0  # Buy signal
        signals['Signal'][moving_average_short < moving_average_long] = -1.0  # Sell signal
        return signals