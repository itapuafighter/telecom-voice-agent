from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String)
    plan_type = Column(String)
    contract_start = Column(DateTime)
    contract_end = Column(DateTime)
    account_status = Column(String)
    postcode = Column(String)

class Outage(Base):
    __tablename__ = "outages"

    id = Column(Integer, primary_key=True, index=True)
    postcode = Column(String, index=True)
    description = Column(String)
    start_time = Column(DateTime)
    estimated_resolution = Column(DateTime)
    status = Column(String)

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    language_detected = Column(String)
    query_type = Column(String)
    resolution_status = Column(String)
    duration_seconds = Column(Integer)
    notes = Column(String)