from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database.db import get_db
from database.models import Interaction
import datetime

router = APIRouter()

class InteractionLog(BaseModel):
    account_number: str
    language_detected: str
    query_type: str
    resolution_status: str
    duration_seconds: int
    notes: str = ""

@router.post("/log")
def log_interaction(log: InteractionLog, db: Session = Depends(get_db)):
    try:
        interaction = Interaction(
            account_number=log.account_number,
            timestamp=datetime.datetime.utcnow(),
            language_detected=log.language_detected,
            query_type=log.query_type,
            resolution_status=log.resolution_status,
            duration_seconds=log.duration_seconds,
            notes=log.notes
        )

        db.add(interaction)
        db.commit()

        return {
            "success": True,
            "message": "Interaction logged successfully."
        }

    except Exception as e:
        return {
            "success": False,
            "message": "Unable to log interaction at this time."
        }