from celery import Celery
import time

app = Celery('worker', broker='redis://redis:6379/0')

@app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=5)
def send_event(self, event):
    try:
        print(f"[Consumer] Processed Event: {event}")
        # Simulate processing time
        time.sleep(5)
    except Exception as exc:
        print(f"Error processing event: {exc}")
        raise self.retry(exc=exc)