#Lets users filter/search events by user_id and event_type.
# This router provides an endpoint to retrieve analytics data based on optional query parameters.

from fastapi import APIRouter
from typing import Optional
from datetime import datetime

router = APIRouter()

@router.get("/analytics")
def get_analytics(user_id: Optional[int] = None, event_type: Optional[str] = None):
    return {
        "results": [
            {
                "user_id": user_id or 123,
                "event_type": event_type or "click",
                "timestamp": datetime.now().isoformat()
            }
        ]
    }