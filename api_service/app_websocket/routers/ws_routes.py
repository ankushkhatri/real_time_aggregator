#WebSocket endpoint to stream live data (events, metrics, alerts).
#Enables real-time dashboards and updates

import asyncio
import redis
from fastapi import APIRouter, WebSocket
from dotenv import load_dotenv
import os
import json
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

router = APIRouter(prefix="/ws", tags=["WebSocket"])
r = redis.Redis(host='redis', port=6379, decode_responses=True)

SYMBOLS = os.getenv("SYMBOLS", "").split(",")

@router.websocket("/live-data")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            prices = {}
            for symbol in SYMBOLS:
                price = r.get(f"crypto:{symbol.upper()}")
                if price:
                    prices[symbol.upper()] = price
            if prices:
                await websocket.send_text(json.dumps(prices))
                print("Sent to WebSocket client:", prices)
            else:
                print("No prices available in Redis.")
            await asyncio.sleep(1) 
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

# This WebSocket endpoint streams live cryptocurrency prices from Redis.
# It connects to the Redis database to fetch the latest BTCUSDT price and sends updates to connected clients every second.