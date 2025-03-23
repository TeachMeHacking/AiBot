import MetaTrader5 as mt5
import pandas as pd
import numpy as np

# Initialize MT5 and login
def mt5_login(login, password, server):
    if not mt5.initialize(login=login, password=password, server=server):
        print("MT5 initialization failed:", mt5.last_error())
        quit()
    else:
        print(f"Logged in to account: {login}")

# Fetch historical data from MT5
def fetch_historical_data(symbol, timeframe, num_bars):
    timeframe_mapping = {
        'M1': mt5.TIMEFRAME_M1,
        'H1': mt5.TIMEFRAME_H1,
        'D1': mt5.TIMEFRAME_D1
    }
    rates = mt5.copy_rates_from_pos(symbol, timeframe_mapping[timeframe], 0, num_bars)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Fetch live data for predictions
def fetch_live_data(symbol, timeframe='M1', num_bars=10):
    return fetch_historical_data(symbol, timeframe, num_bars)

# Execute a buy/sell trade with risk management
def execute_trade(symbol, action, lot_size, stop_loss, take_profit):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": mt5.ORDER_TYPE_BUY if action == 'buy' else mt5.ORDER_TYPE_SELL,
        "sl": stop_loss,
        "tp": take_profit,
        "deviation": 20,
        "magic": 234000,
        "comment": "AI Trading Robot",
    }
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Trade execution failed: {result.retcode}")
    else:
        print(f"Trade successful: {action}, Lot size: {lot_size}")

# Close MT5 connection
def mt5_logout():
    mt5.shutdown()
