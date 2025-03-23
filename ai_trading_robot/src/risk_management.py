# Risk management logic with $100 capital and 1:100 leverage

def calculate_lot_size(balance, risk_percentage, stop_loss_pips, leverage):
    risk_amount = balance * risk_percentage / 100
    lot_size = risk_amount / (stop_loss_pips * 10 / leverage)
    return round(lot_size, 2)

def calculate_stop_loss_and_take_profit(entry_price, pip_distance):
    stop_loss = entry_price - pip_distance if entry_price else 0
    take_profit = entry_price + pip_distance if entry_price else 0
    return stop_loss, take_profit
