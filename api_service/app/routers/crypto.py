from fastapi import APIRouter
from app.redis_client import redis_client

router = APIRouter(prefix="/crypto", tags=["Crypto"])

@router.get("/{symbol}")
def get_crypto_price(symbol: str):
    key = f"crypto:{symbol.upper()}"
    price = redis_client.get(key)
    if price is None:
        return {"error": f"No price data found for {symbol.upper()}"}
    return {"symbol": symbol.upper(), "price": price}
