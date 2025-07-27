import asyncio
import websockets
import json

async def test_ws():
    uri = "ws://localhost:5000/ws/live-data"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            for symbol, price in data.items():
                print(f"{symbol}: {price}")
            await asyncio.sleep(1) 

asyncio.run(test_ws())
