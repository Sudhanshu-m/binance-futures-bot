import os
import argparse
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *

load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_DEFAULT_RECV_WINDOW = 10000

def place_grid(symbol, side, base_price, grid_size, levels, quantity):
    for i in range(1, levels + 1):
        price = base_price + (i * grid_size) if side.upper() == "SELL" else base_price - (i * grid_size)
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=SIDE_SELL if side.upper() == "SELL" else SIDE_BUY,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(round(price, 2))
            )
            print(f"✅ Grid order {i}/{levels} placed at {price}")
        except Exception as e:
            print(f"❌ Failed to place grid order {i} at {price}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", type=str)
    parser.add_argument("side", choices=["BUY", "SELL"])
    parser.add_argument("base_price", type=float)
    parser.add_argument("grid_size", type=float)
    parser.add_argument("levels", type=int)
    parser.add_argument("quantity", type=float)

    args = parser.parse_args()
    place_grid(args.symbol, args.side, args.base_price, args.grid_size, args.levels, args.quantity)
