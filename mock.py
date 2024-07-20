import random
import datetime
import string
from projv2 import *

# Generate mock data for Person table
def generate_person_data(num_records):
    person_data = []
    for _ in range(num_records):
        firstname = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 15)))
        lastname = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 15)))
        phonenumber = ''.join(random.choices(string.digits, k=10))
        address = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=random.randint(10, 30)))
        city = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 15)))
        state = ''.join(random.choices(string.ascii_uppercase, k=2))
        postalcode = ''.join(random.choices(string.digits, k=5))
        country = 'USA'
        birthdate = datetime.date(random.randint(1950, 2000), random.randint(1, 12), random.randint(1, 28))
        person_data.append((firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate))
    return person_data

# Generate mock data for EmergencyContact table
def generate_emergency_contact_data(num_records, person_ids):
    emergency_contact_data = []
    for personid in random.sample(person_ids, min(num_records, len(person_ids))):
        for _ in range(random.randint(1, 3)):  # 1 to 3 emergency contacts per person
            emergency_contact = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 20)))
            emergency_contact_phone = ''.join(random.choices(string.digits, k=10))
            emergency_contact_workphone = ''.join(random.choices(string.digits, k=10))
            emergency_contact_data.append((personid, emergency_contact, emergency_contact_phone, emergency_contact_workphone))
    return emergency_contact_data

# Generate mock data for Insurance table
def generate_insurance_data(num_records, person_ids):
    insurance_data = []
    for personid in random.sample(person_ids, min(num_records, len(person_ids))):
        insurance_company = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 20)))
        insurance_address = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=random.randint(10, 30)))
        insurance_city = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 15)))
        insurance_state = ''.join(random.choices(string.ascii_uppercase, k=2))
        insurance_postalcode = ''.join(random.choices(string.digits, k=5))
        insurance_country = 'USA'
        policy_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(8, 12)))
        expiry_date = datetime.date(random.randint(2024, 2028), random.randint(1, 12), random.randint(1, 28))
        insurance_data.append((personid, insurance_company, insurance_address, insurance_city, insurance_state, insurance_postalcode, insurance_country, policy_number, expiry_date))
    return insurance_data

# Generate mock data for MedicalHistory table
def generate_medical_history_data(num_records, person_ids):
    medical_history_data = []
    for personid in random.sample(person_ids, min(num_records, len(person_ids))):
        hepatitisb = random.choice([True, False])
        chickenpox = random.choice([True, False])
        measles = random.choice([True, False])
        significant_medical_history = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(20, 100)))
        medical_problems = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(20, 100)))
        medication = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(10, 50)))
        allergies = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(10, 50)))
        medical_history_data.append((personid, hepatitisb, chickenpox, measles, significant_medical_history, medical_problems, medication, allergies))
    return medical_history_data

# Insert mock data into the database
num_person_records = 500
person_data = generate_person_data(num_person_records)
for person in person_data:
    c.execute("INSERT INTO Person (firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", person)
conn.commit()

# Fetch person IDs after inserting
person_ids = []
c.execute("SELECT personid FROM Person")
for row in c.fetchall():
    person_ids.append(row[0])

# Generate and insert emergency contacts
emergency_contact_data = generate_emergency_contact_data(num_person_records, person_ids)
for emergency_contact in emergency_contact_data:
    c.execute("INSERT INTO EmergencyContact (personid, emergencycontact, emergencycontactphone, emergencycontactworkphone) VALUES (%s, %s, %s, %s)", emergency_contact)
conn.commit()

# Generate and insert insurance data
insurance_data = generate_insurance_data(num_person_records, person_ids)
for insurance in insurance_data:
    c.execute("INSERT INTO Insurance (personid, insurancecompany, insuranceaddress, insurancecity, insurancestate, insurancepostalcode, insurancecountry, policynumber, expirydate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", insurance)
conn.commit()

# Generate and insert medical history data
medical_history_data = generate_medical_history_data(num_person_records, person_ids)
for medical_history in medical_history_data:
    c.execute("INSERT INTO MedicalHistory (personid, hepatitisb, chickenpox, measles, significantmedicalhistory, medicalproblems, medication, allergies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", medical_history)
conn.commit()
