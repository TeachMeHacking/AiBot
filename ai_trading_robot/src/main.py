from mt5_interface import mt5_login, mt5_logout, fetch_live_data, execute_trade
from risk_management import calculate_lot_size, calculate_stop_loss_and_take_profit
from ai_model import train_model, load_trained_model
from trade_memory import update_trade_memory, learn_from_trade_memory
import MetaTrader5 as mt5

# Login to MT5
mt5_login(login=123456, password='password', server='broker_server')

# Load trained AI model or train a new one
try:
    model = load_trained_model()
except FileNotFoundError:
    df = load_data()
    model = train_model(df)

# Fetch live data for decision-making
symbol = 'XAUUSD'
live_data = fetch_live_data(symbol)

# Use the AI model to predict buy/sell signals
prediction = model.predict(live_data[['SMA_50', 'liquidity_zone', 'bos']])
action = 'buy' if prediction == 1 else 'sell'

# Risk management
balance = mt5.account_info().balance
lot_size = calculate_lot_size(balance, risk_percentage=1, stop_loss_pips=50, leverage=100)
stop_loss, take_profit = calculate_stop_loss_and_take_profit(live_data['close'].iloc[-1], pip_distance=50)

# Execute trade
execute_trade(symbol, action, lot_size, stop_loss, take_profit)

# Save trade information to memory and learn from it
update_trade_memory({
    "symbol": symbol,
    "action": action,
    "lot_size": lot_size,
    "profit": learn_from_trade_memory()
})

# Logout from MT5
mt5_logout()
