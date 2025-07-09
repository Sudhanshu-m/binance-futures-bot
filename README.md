# 📊 Binance Futures Trading Bot – Python (Testnet)

## 📘 Project Overview

This is a modular Python-based trading bot designed to execute **Market**, **Limit**, and **Advanced Orders** on Binance's **USDT-M Futures Testnet**.  
Built as part of an internship project, it includes CLI scripts, environment-secure API handling, logging, and strategy-based automation.

---

## 📌 Objectives

- Connect securely to Binance Testnet via API
- Execute Market and Limit orders via CLI
- Simulate OCO (TP + SL) orders
- Automate order slicing using TWAP
- Deploy grid-based order strategies
- Maintain clean logs and clear project structure

---

## ⚙️ Technologies Used

- Python 3.8+
- `python-binance` (official Binance API SDK)
- `python-dotenv` for .env key loading
- Binance USDT-M Futures Testnet
- Git + GitHub for version control
- PyCharm (for development)
- CLI / Terminal

---

## 🔐 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/binance-futures-bot.git
cd binance-futures-bot
```

### 2. Create `.env` file in root
```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

### 3. Install dependencies
```bash
pip install python-binance python-dotenv
```

---

## 📁 Project Structure

```
binance-futures-bot/
├── .env                  # API credentials (not uploaded)
├── bot.log               # Order logs
├── report.pdf            # Final project documentation
├── README.md             # This file
├── .gitignore            # Hides .env, logs
└── src/
    ├── market_orders.py      # CLI: Market orders
    ├── limit_orders.py       # CLI: Limit orders
    └── advanced/
        ├── oco.py            # Simulated OCO (TP+SL)
        ├── twap.py           # TWAP execution
        └── grid_orders.py    # Grid strategy
```

---

## 🚀 CLI Usage Examples

### Market Order:
```bash
python src/market_orders.py BTCUSDT BUY 0.01
```

### Limit Order:
```bash
python src/limit_orders.py BTCUSDT SELL 0.01 65000
```

### Simulated OCO:
```bash
python src/advanced/oco.py BTCUSDT BUY 0.01 67000 63000
```

### TWAP Order:
```bash
python src/advanced/twap.py BTCUSDT BUY 0.05 5 10
```

### Grid Order:
```bash
python src/advanced/grid_orders.py BTCUSDT BUY 65000 100 3 0.01
```

---

## 📄 Logging

All events are recorded in `bot.log` for:
- Order IDs
- Execution success/failure
- Errors and exceptions

---

## 🧪 Testing

All strategies were tested on:  
🔗 [https://testnet.binancefuture.com/en/futures/BTCUSDT](https://testnet.binancefuture.com/en/futures/BTCUSDT)

Testnet credentials used. Screenshots of filled orders are available in `report.pdf`.

---

## 🧾 Submission Components

- ✅ `src/` folder with all Python scripts
- ✅ `.env` for credentials 
- ✅ `bot.log` for logs
- ✅ `README.md` with full setup guide
- ✅ `report.pdf` with screenshots and explanation

---

## 👨‍💻 Author

Sudhanshu Mishra