import urllib.request, json

def quote(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = json.loads(urllib.request.urlopen(req).read())
    price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    print(f"{symbol}: ${price}")

if __name__ == "__main__":
    quote(input("Ticker (e.g., AAPL): ").upper())