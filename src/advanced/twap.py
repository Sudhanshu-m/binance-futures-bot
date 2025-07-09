import os
import time
import argparse
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *

load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_DEFAULT_RECV_WINDOW = 10000

def twap_order(symbol, side, total_quantity, slices, interval_sec):
    slice_qty = round(total_quantity / slices, 6)
    print(f"🚀 TWAP: {slices} orders of {slice_qty} {symbol} every {interval_sec}s")

    for i in range(slices):
        try:
            client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=slice_qty
            )
            print(f"✅ Order {i+1}/{slices} placed")
            time.sleep(interval_sec)
        except Exception as e:
            print(f"❌ Failed at order {i+1}: {e}")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", type=str)
    parser.add_argument("side", choices=["BUY", "SELL"])
    parser.add_argument("total_quantity", type=float)
    parser.add_argument("slices", type=int)
    parser.add_argument("interval", type=int)

    args = parser.parse_args()
    twap_order(args.symbol, args.side, args.total_quantity, args.slices, args.interval)
