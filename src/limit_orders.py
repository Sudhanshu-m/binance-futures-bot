import os
import argparse
import logging
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *

# Load API keys
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Set up logging
logging.basicConfig(filename="bot.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Binance client (Testnet)
client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_DEFAULT_RECV_WINDOW = 10000  # 10 seconds drift allowed

def place_limit_order(symbol: str, side: str, quantity: float, price: float):
    try:
        side_enum = SIDE_BUY if side.upper() == "BUY" else SIDE_SELL
        order = client.futures_create_order(
            symbol=symbol,
            side=side_enum,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(price)
        )
        logging.info(f"Limit Order: {side} {quantity} {symbol} @ {price} | Order ID: {order['orderId']}")
        print(f"✅ Limit order placed: {side} {quantity} {symbol} @ {price}")
    except Exception as e:
        logging.error(f"Limit order error: {e}")
        print("❌ Error placing limit order:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", type=str, help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("side", choices=["BUY", "SELL"], help="Order direction")
    parser.add_argument("quantity", type=float, help="Order amount")
    parser.add_argument("price", type=float, help="Limit price")
    args = parser.parse_args()
    place_limit_order(args.symbol, args.side, args.quantity, args.price)
