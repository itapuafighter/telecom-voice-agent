from fastapi import APIRouter
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class EmailRequest(BaseModel):
    to_email: str
    subject: str
    message: str
    customer_name: str

@router.post("/email")
def send_email(request: EmailRequest):
    try:
        # For now we mock the email send
        # In production replace with SendGrid or Gmail SMTP
        print(f"📧 Email would be sent to: {request.to_email}")
        print(f"   Subject: {request.subject}")
        print(f"   Message: {request.message}")

        return {
            "success": True,
            "message": f"Confirmation email sent to {request.to_email}"
        }

    except Exception as e:
        return {
            "success": False,
            "message": "Unable to send confirmation email at this time."
        }