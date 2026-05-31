from fastapi import FastAPI
from database.db import init_db
from tools import account, outage, billing, email_service, log

app = FastAPI(title="Telecom Voice Agent")

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Register tool routers
app.include_router(account.router, prefix="/tools")
app.include_router(outage.router, prefix="/tools")
app.include_router(billing.router, prefix="/tools")
app.include_router(email_service.router, prefix="/tools")
app.include_router(log.router, prefix="/tools")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Telecom Voice Agent running"}