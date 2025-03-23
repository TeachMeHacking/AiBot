import json

# Store trade history in a file and learn from it
def load_trade_memory(filename='data/trade_history.json'):
    try:
        with open(filename, 'r') as file:
            trade_history = json.load(file)
    except FileNotFoundError:
        trade_history = []
    return trade_history

def save_trade_memory(trades, filename='data/trade_history.json'):
    with open(filename, 'w') as file:
        json.dump(trades, file, indent=4)

def update_trade_memory(trade):
    trade_history = load_trade_memory()
    trade_history.append(trade)
    save_trade_memory(trade_history)

def learn_from_trade_memory():
    trade_history = load_trade_memory()
    # Analyze past trades, calculate patterns, and adjust AI decision-making
    profits = [trade['profit'] for trade in trade_history]
    return sum(profits) / len(profits) if profits else 0
