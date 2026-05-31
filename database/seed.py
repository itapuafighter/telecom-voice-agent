from database.db import SessionLocal, init_db
from database.models import Customer, Outage
import datetime

def seed():
    init_db()
    db = SessionLocal()

    # Clear existing data
    db.query(Customer).delete()
    db.query(Outage).delete()
    db.commit()

    # Fake customers
    customers = [
        Customer(
            account_number="ACC001",
            phone_number="+34600000001",
            name="Carlos García",
            email="carlos.garcia@email.com",
            plan_type="Fibra 600MB",
            contract_start=datetime.datetime(2023, 1, 15),
            contract_end=datetime.datetime(2025, 1, 15),
            account_status="active",
            postcode="28001"
        ),
        Customer(
            account_number="ACC002",
            phone_number="+34600000002",
            name="María López",
            email="maria.lopez@email.com",
            plan_type="Fibra 1GB",
            contract_start=datetime.datetime(2022, 6, 1),
            contract_end=datetime.datetime(2024, 6, 1),
            account_status="active",
            postcode="28002"
        ),
        Customer(
            account_number="ACC003",
            phone_number="+34600000003",
            name="James Smith",
            email="james.smith@email.com",
            plan_type="Móvil 20GB",
            contract_start=datetime.datetime(2023, 3, 10),
            contract_end=datetime.datetime(2025, 3, 10),
            account_status="active",
            postcode="28003"
        ),
        Customer(
            account_number="ACC004",
            phone_number="+34600000004",
            name="Sophie Müller",
            email="sophie.muller@email.com",
            plan_type="Fibra 600MB + Móvil 10GB",
            contract_start=datetime.datetime(2022, 11, 20),
            contract_end=datetime.datetime(2024, 11, 20),
            account_status="suspended",
            postcode="28004"
        ),
        Customer(
            account_number="ACC005",
            phone_number="+34600000005",
            name="Pierre Dubois",
            email="pierre.dubois@email.com",
            plan_type="Fibra 1GB + Móvil 50GB",
            contract_start=datetime.datetime(2023, 7, 5),
            contract_end=datetime.datetime(2025, 7, 5),
            account_status="active",
            postcode="28005"
        ),
        Customer(
            account_number="ACC006",
            phone_number="+34600000006",
            name="Ana Martínez",
            email="ana.martinez@email.com",
            plan_type="Móvil 50GB",
            contract_start=datetime.datetime(2023, 2, 28),
            contract_end=datetime.datetime(2025, 2, 28),
            account_status="active",
            postcode="28006"
        ),
        Customer(
            account_number="ACC007",
            phone_number="+34600000007",
            name="Thomas Schneider",
            email="thomas.schneider@email.com",
            plan_type="Fibra 600MB",
            contract_start=datetime.datetime(2022, 9, 1),
            contract_end=datetime.datetime(2024, 9, 1),
            account_status="active",
            postcode="28001"
        ),
        Customer(
            account_number="ACC008",
            phone_number="+34600000008",
            name="Laura Fernández",
            email="laura.fernandez@email.com",
            plan_type="Fibra 1GB",
            contract_start=datetime.datetime(2023, 5, 15),
            contract_end=datetime.datetime(2025, 5, 15),
            account_status="active",
            postcode="28003"
        ),
        Customer(
            account_number="ACC009",
            phone_number="+34600000009",
            name="Marco Rossi",
            email="marco.rossi@email.com",
            plan_type="Móvil 20GB",
            contract_start=datetime.datetime(2022, 12, 1),
            contract_end=datetime.datetime(2024, 12, 1),
            account_status="active",
            postcode="28007"
        ),
        Customer(
            account_number="ACC010",
            phone_number="+34600000010",
            name="Elena Sánchez",
            email="elena.sanchez@email.com",
            plan_type="Fibra 600MB + Móvil 20GB",
            contract_start=datetime.datetime(2023, 8, 20),
            contract_end=datetime.datetime(2025, 8, 20),
            account_status="active",
            postcode="28002"
        ),
    ]

    # Fake outages
    outages = [
        Outage(
            postcode="28001",
            description="Interrupción de fibra óptica por obras en la calle",
            start_time=datetime.datetime.utcnow() - datetime.timedelta(hours=2),
            estimated_resolution=datetime.datetime.utcnow() + datetime.timedelta(hours=4),
            status="active"
        ),
        Outage(
            postcode="28003",
            description="Mantenimiento programado de la red",
            start_time=datetime.datetime.utcnow() - datetime.timedelta(hours=1),
            estimated_resolution=datetime.datetime.utcnow() + datetime.timedelta(hours=2),
            status="active"
        ),
        Outage(
            postcode="28007",
            description="Fallo en el nodo de distribución",
            start_time=datetime.datetime.utcnow() - datetime.timedelta(hours=3),
            estimated_resolution=datetime.datetime.utcnow() + datetime.timedelta(hours=6),
            status="active"
        ),
    ]

    db.add_all(customers)
    db.add_all(outages)
    db.commit()
    db.close()

    print("✅ Database seeded successfully")
    print(f"   → {len(customers)} customers added")
    print(f"   → {len(outages)} outages added")

if __name__ == "__main__":
    seed()