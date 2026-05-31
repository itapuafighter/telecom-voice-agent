from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Customer

router = APIRouter()

@router.get("/account")
def get_account(identifier: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(
        (Customer.account_number == identifier) |
        (Customer.phone_number == identifier)
    ).first()

    if not customer:
        return {"error": "Account not found. Please check the number and try again."}

    return {
        "account_number": customer.account_number,
        "name": customer.name,
        "plan_type": customer.plan_type,
        "contract_start": customer.contract_start.strftime("%d/%m/%Y"),
        "contract_end": customer.contract_end.strftime("%d/%m/%Y"),
        "account_status": customer.account_status,
        "postcode": customer.postcode,
        "email": customer.email
    }