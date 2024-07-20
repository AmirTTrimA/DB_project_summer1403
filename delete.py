from projv2 import *

def clear_database():
    tables = ["MedicalHistory", "Insurance", "EmergencyContact", "Person"]
    for table in tables:
        c.execute(f"DELETE FROM {table}")
    conn.commit()

# Call clear_database function before inserting new mock data
clear_database()
