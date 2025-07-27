import asyncio
import websockets
import json
import redis 
from dotenv import load_dotenv
import os

load_dotenv()

r = redis.Redis(host='redis', port=6379, decode_responses=True)

SYMBOLS = os.getenv("SYMBOLS", "").split(",")

async def consume(symbol):
    print('symbol:', symbol)
    url = f"wss://stream.binance.com:9443/ws/{symbol}@ticker"
    async with websockets.connect(url) as websocket:
        print(f"Connected to Binance WebSocket for {symbol.upper()}")
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                price = data.get('c') # get the last price
                if price:
                    print(f"{symbol.upper()} Price: {price}")
                    # Store the price in Redis
                    r.set(f"crypto:{symbol.upper()}", price)
            except Exception as e:
                print(f"[Error] {symbol.upper()} - {e}")
                await asyncio.sleep(5) 

async def main():
    tasks = [consume(symbol) for symbol in SYMBOLS]
    await asyncio.gather(*tasks)

if __name__ == "__main__": 
    asyncio.run(main())

# This script connects to Binance WebSocket API to fetch live cryptocurrency prices for BTCUSDT, ETHUSDT, and BNBUSDT.
# It stores the latest prices in a Redis database