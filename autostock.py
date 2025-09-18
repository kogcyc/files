import yfinance as yf

# Define stock symbols and scalars
stocks = {
    "AMZN": 200,
    "NVDA": 250,
    "PLTR": 190
}

total = 0.0

for symbol, scalar in stocks.items():
    ticker = yf.Ticker(symbol)
    price = ticker.history(period="1d")["Close"].iloc[-1]  # latest close price
    product = price * scalar
    print(f"{symbol}: price={price:.2f}, scalar={scalar}, product={product:.2f}")
    total += product

print(f"\nTotal sum = {total:.2f}")
