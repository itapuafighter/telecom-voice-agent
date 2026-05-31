from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Customer
import datetime

router = APIRouter()

@router.get("/billing")
def get_billing(account_number: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(
        Customer.account_number == account_number
    ).first()

    if not customer:
        return {"error": "Account not found. Please check the number and try again."}

    # Mock billing data based on plan type
    billing_data = {
        "Fibra 600MB": {"monthly_fee": 39.99, "currency": "EUR"},
        "Fibra 1GB": {"monthly_fee": 49.99, "currency": "EUR"},
        "Móvil 20GB": {"monthly_fee": 19.99, "currency": "EUR"},
        "Móvil 50GB": {"monthly_fee": 29.99, "currency": "EUR"},
        "Fibra 600MB + Móvil 10GB": {"monthly_fee": 54.99, "currency": "EUR"},
        "Fibra 600MB + Móvil 20GB": {"monthly_fee": 59.99, "currency": "EUR"},
        "Fibra 1GB + Móvil 50GB": {"monthly_fee": 74.99, "currency": "EUR"},
    }

    plan = billing_data.get(customer.plan_type, {"monthly_fee": 39.99, "currency": "EUR"})

    # Mock billing cycle - due on the 1st of next month
    today = datetime.date.today()
    if today.month == 12:
        due_date = datetime.date(today.year + 1, 1, 1)
    else:
        due_date = datetime.date(today.year, today.month + 1, 1)

    return {
        "account_number": customer.account_number,
        "name": customer.name,
        "plan_type": customer.plan_type,
        "monthly_fee": plan["monthly_fee"],
        "currency": plan["currency"],
        "due_date": due_date.strftime("%d/%m/%Y"),
        "account_status": customer.account_status
    }