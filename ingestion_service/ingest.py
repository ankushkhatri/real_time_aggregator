# Async ingestion from APIs/files

import time 
from datetime import datetime
from celery import Celery
import os

app = Celery('ingest', broker=os.getenv("CELERY_BROKER_URL"))

@app.task
def send_event(event):
    time.sleep(5)
    
def generate_event():
    return {
        "user_id": 123,
        "event_type": "click",
        "timestamp": datetime.now().isoformat(),
    }
    
if __name__ == "__main__":
    # while True:
    event = generate_event()
    send_event.delay(event)
    print(f"[Producer] Event sent: {event}")
    time.sleep(5)
    # This will run the task asynchronously using Celery with Redis as the broker.

