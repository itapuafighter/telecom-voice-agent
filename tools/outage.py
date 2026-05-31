from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Outage

router = APIRouter()

@router.get("/outage")
def check_outage(postcode: str, db: Session = Depends(get_db)):
    outage = db.query(Outage).filter(
        Outage.postcode == postcode,
        Outage.status == "active"
    ).first()

    if not outage:
        return {
            "outage_detected": False,
            "message": "No active outages detected in your area."
        }

    return {
        "outage_detected": True,
        "description": outage.description,
        "start_time": outage.start_time.strftime("%d/%m/%Y %H:%M"),
        "estimated_resolution": outage.estimated_resolution.strftime("%d/%m/%Y %H:%M"),
        "status": outage.status
    }