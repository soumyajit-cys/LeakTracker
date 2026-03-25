from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import os
from dotenv import load_dotenv

from app.routes import keyword_routes, breach_routes, alert_routes, scan_routes
from app.services.scan_service import run_scan

load_dotenv()

app = FastAPI(title="LeakSentinel Backend")

app.include_router(keyword_routes.router)
app.include_router(breach_routes.router)
app.include_router(alert_routes.router)
app.include_router(scan_routes.router)

scheduler = BackgroundScheduler()
scheduler.add_job(run_scan, "interval", seconds=int(os.getenv("SCAN_INTERVAL", 60)))
scheduler.start()

@app.get("/")
def root():
    return {"message": "LeakSentinel Running"}