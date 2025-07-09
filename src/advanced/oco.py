import os
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *
ORDER_TYPE_STOP_MARKET = "STOP_MARKET"


load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_DEFAULT_RECV_WINDOW = 10000

def place_simulated_oco(symbol, side, quantity, take_profit_price, stop_price):
    opposite = SIDE_SELL if side.upper() == "BUY" else SIDE_BUY
    try:
        # Take Profit
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=opposite,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(take_profit_price)
        )

        # Stop Loss
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=opposite,
            type=ORDER_TYPE_STOP_MARKET,
            stopPrice=str(stop_price),
            closePosition=True
        )

        print("✅ Simulated OCO: TP and SL orders placed.")
    except Exception as e:
        print("❌ Failed to place simulated OCO:", e)

if __name__ == "__main__":
    place_simulated_oco("BTCUSDT", "BUY", 0.01, 67000, 63000)
