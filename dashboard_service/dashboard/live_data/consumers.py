import asyncio
import websockets
import json
import redis 
from dotenv import load_dotenv
import os
from channels.generic.websocket import AsyncWebsocketConsumer

load_dotenv()

r = redis.Redis(host='redis', port=6379, decode_responses=True)

class LiveDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_sending = True
        asyncio.create_task(self.send_prices())

    async def disconnect(self, close_code):
        self.keep_sending = False

    async def send_prices(self):
        while self.keep_sending:
            prices = {}
            for symbol in os.getenv("SYMBOLS", "").split(","):
                price = r.get(f"crypto:{symbol.upper()}")
                if price:
                    prices[symbol.upper()] = price
            if prices:
                await self.send(text_data=json.dumps(prices))
            await asyncio.sleep(1)