# Telecom Customer Support Voice Agent

A multilingual voice AI agent for telecom customer support, built on ElevenLabs Conversational AI.

## What it does

This project demonstrates a voice-based customer support agent that handles inbound queries in multiple languages (Spanish, English, German, French). The agent can look up customer accounts, check for service outages, retrieve billing information, send confirmation emails, and log all interactions.

## Architecture

```
Voice Input → ElevenLabs Agent → FastAPI Backend → SQLite Database
                    ↓
            [Account Lookup Tool]
            [Outage Check Tool]
            [Billing Tool]
            [Email Service Tool]
            [Interaction Logging Tool]
```

## Features

- ✅ Multilingual support: Spanish, English, German, French
- ✅ Real-time account lookup by account number or phone number
- ✅ Outage detection by postcode
- ✅ Billing information retrieval
- ✅ Automated confirmation emails
- ✅ Full interaction logging and analytics
- ✅ Production-grade error handling and fallbacks

## Tech Stack

| Component | Technology |
|---|---|
| Voice AI | ElevenLabs Conversational AI |
| Backend | Python + FastAPI |
| Database | SQLite |
| Language Detection | ElevenLabs native |
| Deployment | ngrok (local tunneling) |

## Setup

### Prerequisites
- Python 3.9+
- ElevenLabs API key
- ngrok account (free tier)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/itapuafighter/telecom-voice-agent.git
cd telecom-voice-agent
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# .\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

5. Add your ElevenLabs API key to `.env`:
```
ELEVENLABS_API_KEY=your_key_here
SENDGRID_API_KEY=your_key_here
DATABASE_URL=sqlite:///./telecom.db
```

6. Start the FastAPI backend:
```bash
uvicorn main:app --reload
```

7. In a new terminal, expose local server with ngrok:
```bash
ngrok http 8000
```

8. Copy the ngrok URL and configure it in ElevenLabs agent tool endpoints.

## API Endpoints

All endpoints are under `/tools/`:

### GET /tools/account
Look up customer account by account number or phone number.

**Parameters:**
- `identifier` (string, required): Account number (e.g., ACC001) or phone number

**Response:**
```json
{
  "account_number": "ACC001",
  "name": "Carlos García",
  "plan_type": "Fibra 600MB",
  "contract_start": "15/01/2023",
  "contract_end": "15/01/2025",
  "account_status": "active",
  "postcode": "28001",
  "email": "carlos.garcia@email.com"
}
```

### GET /tools/outage
Check for active outages in a specific postcode.

**Parameters:**
- `postcode` (string, required): Customer's postcode

**Response (outage found):**
```json
{
  "outage_detected": true,
  "description": "Interrupción de fibra óptica por obras en la calle",
  "start_time": "31/05/2026 14:45",
  "estimated_resolution": "31/05/2026 20:45",
  "status": "active"
}
```

### GET /tools/billing
Retrieve billing information for a customer.

**Parameters:**
- `account_number` (string, required): Customer's account number

**Response:**
```json
{
  "account_number": "ACC001",
  "name": "Carlos García",
  "plan_type": "Fibra 600MB",
  "monthly_fee": 39.99,
  "currency": "EUR",
  "due_date": "01/06/2026",
  "account_status": "active"
}
```

### POST /tools/email
Send a confirmation email to the customer.

**Body:**
```json
{
  "to_email": "customer@email.com",
  "subject": "Your support ticket",
  "message": "Your issue has been logged",
  "customer_name": "Carlos García"
}
```

### POST /tools/log
Log the interaction to the database.

**Body:**
```json
{
  "account_number": "ACC001",
  "language_detected": "Spanish",
  "query_type": "account_lookup",
  "resolution_status": "resolved",
  "duration_seconds": 180,
  "notes": "Customer satisfied with outage update"
}
```

## Database Schema

### customers
- `id` (int, primary key)
- `account_number` (string, unique)
- `phone_number` (string, unique)
- `name` (string)
- `email` (string)
- `plan_type` (string)
- `contract_start` (datetime)
- `contract_end` (datetime)
- `account_status` (string)
- `postcode` (string)

### outages
- `id` (int, primary key)
- `postcode` (string, indexed)
- `description` (string)
- `start_time` (datetime)
- `estimated_resolution` (datetime)
- `status` (string)

### interactions
- `id` (int, primary key)
- `account_number` (string)
- `timestamp` (datetime, auto-set)
- `language_detected` (string)
- `query_type` (string)
- `resolution_status` (string)
- `duration_seconds` (int)
- `notes` (string)

## Design Decisions

### Why ElevenLabs Conversational AI?
ElevenLabs handles the hard parts — speech to text, turn-taking, interruption handling, text to speech. You focus on the business logic and tools.

### Why FastAPI?
FastAPI is async by default, has automatic API documentation, and is production-ready. It's the modern choice for Python backends.

### Why SQLite for a demo?
SQLite is sufficient for portfolio purposes and keeps setup simple. In production you'd use PostgreSQL on RDS or Supabase. The abstraction layer in `database/db.py` makes swapping trivial.

### Multilingual Approach
ElevenLabs detects the language from the user's speech and responds natively. The system prompt instructs the agent to match the customer's language without custom language detection code.

## Production Readiness

To make this production-ready:
- Replace SQLite with PostgreSQL
- Add real authentication (not just account number lookup)
- Implement rate limiting on tool endpoints
- Use proper secrets management (AWS Secrets Manager, HashiCorp Vault)
- Deploy on a real server instead of ngrok
- Add monitoring and alerting (DataDog, New Relic)
- Implement proper error tracking (Sentry)
- Add comprehensive logging
- Use a real email service with proper queuing

## Why I Built This

I have 7 years of experience in telecom customer support. This project applies that real-world knowledge to voice AI — the queries the agent handles, the way it escalates, the interaction logging, the outage checking. These aren't hypothetical; they're based on actual customer pain points I've seen and solved.

## Next Steps

- [ ] Improve multilingual language detection and response matching
- [ ] Add more tool endpoints (SIM card status, contract modifications, payment processing)
- [ ] Implement real SendGrid email integration
- [ ] Add conversation analytics dashboard
- [ ] Create mobile app wrapper
- [ ] Deploy to production infrastructure

## License

MIT
