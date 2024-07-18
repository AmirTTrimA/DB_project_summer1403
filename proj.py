import psycopg2
import tkinter as tk
from tkinter import *
from tkinter import ttk


# Connect to the PostgreSQL database on the university server
conn = psycopg2.connect(
    host="78.38.35.219",
    port="5432",
    database="400463146",
    user="400463146",
    password="123456"
)
c = conn.cursor()

# Create the necessary tables
c.execute('''CREATE TABLE IF NOT EXISTS Person (
             personid SERIAL PRIMARY KEY,
             firstname TEXT,
             lastname TEXT,
             phonenumber TEXT,
             address TEXT,
             city TEXT,
             state TEXT,
             postalcode TEXT,
             country TEXT,
             birthdate DATE)''')

c.execute('''CREATE TABLE IF NOT EXISTS EmergencyContact (
             emergencycontactid SERIAL PRIMARY KEY,
             personid INTEGER,
             emergencycontact TEXT,
             emergencycontactphone TEXT,
             emergencycontactworkphone TEXT,
             FOREIGN KEY (personid) REFERENCES Person(personid))''')

c.execute('''CREATE TABLE IF NOT EXISTS Insurance (
             insuranceid SERIAL PRIMARY KEY,
             personid INTEGER,
             insurancecompany TEXT,
             insuranceaddress TEXT,
             insurancecity TEXT,
             insurancestate TEXT,
             insurancepostalcode TEXT,
             insurancecountry TEXT,
             policynumber TEXT,
             expirydate DATE,
             FOREIGN KEY (personid) REFERENCES Person(personid))''')

c.execute('''CREATE TABLE IF NOT EXISTS MedicalHistory (
             medicalhistoryid SERIAL PRIMARY KEY,
             personid INTEGER,
             hepatitisb BOOLEAN,
             chickenpox BOOLEAN,
             measles BOOLEAN,
             significantmedicalhistory TEXT,
             medicalproblems TEXT,
             medication TEXT,
             allergies TEXT,
             FOREIGN KEY (personid) REFERENCES Person(personid))''')

# Create the CRUD forms
class PersonForm(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Labels for the form fields
        firstname_label = tk.Label(self, text="First Name:")
        lastname_label = tk.Label(self, text="Last Name:")
        phonenumber_label = tk.Label(self, text="Phone Number:")
        address_label = tk.Label(self, text="Address:")
        city_label = tk.Label(self, text="City:")
        state_label = tk.Label(self, text="State:")
        postalcode_label = tk.Label(self, text="Postal Code:")
        country_label = tk.Label(self, text="Country:")
        birthdate_label = tk.Label(self, text="Birthdate:")

        # Form fields
        self.firstname_entry = tk.Entry(self)
        self.lastname_entry = tk.Entry(self)
        self.phonenumber_entry = tk.Entry(self)
        self.address_entry = tk.Entry(self)
        self.city_entry = tk.Entry(self)
        self.state_entry = tk.Entry(self)
        self.postalcode_entry = tk.Entry(self)
        self.country_entry = tk.Entry(self)
        self.birthdate_entry = tk.Entry(self)

        # Grid layout
        firstname_label.grid(row=0, column=0)
        self.firstname_entry.grid(row=0, column=1)
        lastname_label.grid(row=1, column=0)
        self.lastname_entry.grid(row=1, column=1)
        phonenumber_label.grid(row=2, column=0)
        self.phonenumber_entry.grid(row=2, column=1)
        address_label.grid(row=3, column=0)
        self.address_entry.grid(row=3, column=1)
        city_label.grid(row=4, column=0)
        self.city_entry.grid(row=4, column=1)
        state_label.grid(row=5, column=0)
        self.state_entry.grid(row=5, column=1)
        postalcode_label.grid(row=6, column=0)
        self.postalcode_entry.grid(row=6, column=1)
        country_label.grid(row=7, column=0)
        self.country_entry.grid(row=7, column=1)
        birthdate_label.grid(row=8, column=0)
        self.birthdate_entry.grid(row=8, column=1)

        # Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_person)
        self.save_button.grid(row=9, column=1)

        # Status label
        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=10, column=1)

    def save_person(self):
        try:
            firstname = self.firstname_entry.get()
            lastname = self.lastname_entry.get()
            phonenumber = self.phonenumber_entry.get()
            address = self.address_entry.get()
            city = self.city_entry.get()
            state = self.state_entry.get()
            postalcode = self.postalcode_entry.get()
            country = self.country_entry.get()
            birthdate = self.birthdate_entry.get()

            c.execute("INSERT INTO Person (firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate))
            conn.commit()

            self.firstname_entry.delete(0, tk.END)
            self.lastname_entry.delete(0, tk.END)
            self.phonenumber_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.city_entry.delete(0, tk.END)
            self.state_entry.delete(0, tk.END)
            self.postalcode_entry.delete(0, tk.END)
            self.country_entry.delete(0, tk.END)
            self.birthdate_entry.delete(0, tk.END)

            self.status_label.config(text="Data saved successfully!", fg="green")
        except (psycopg2.Error) as e:
            self.status_label.config(text=f"Error saving data: {e}", fg="red")



class EmergencyContactForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Labels for the form fields
        emergencycontact_label = tk.Label(self, text="Emergency Contact:")
        emergencycontactphone_label = tk.Label(self, text="Emergency Contact Phone:")
        emergencycontactworkphone_label = tk.Label(self, text="Emergency Contact Work Phone:")

        # Form fields
        self.emergencycontact_entry = tk.Entry(self)
        self.emergencycontactphone_entry = tk.Entry(self)
        self.emergencycontactworkphone_entry = tk.Entry(self)

        # Grid layout
        emergencycontact_label.grid(row=0, column=0)
        self.emergencycontact_entry.grid(row=0, column=1)
        emergencycontactphone_label.grid(row=1, column=0)
        self.emergencycontactphone_entry.grid(row=1, column=1)
        emergencycontactworkphone_label.grid(row=2, column=0)
        self.emergencycontactworkphone_entry.grid(row=2, column=1)

        # Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_emergency_contact)
        self.save_button.grid(row=3, column=1)

        # Status label
        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=4, column=1)

    def save_emergency_contact(self, personid):
        try:
            emergencycontact = self.emergencycontact_entry.get()
            emergencycontactphone = self.emergencycontactphone_entry.get()
            emergencycontactworkphone = self.emergencycontactworkphone_entry.get()

            # Save the emergency contact data to the database
            c.execute("INSERT INTO EmergencyContact (personid, emergencycontact, emergencycontactphone, emergencycontactworkphone) VALUES (%s, %s, %s, %s)", 
                  (personid, emergencycontact, emergencycontactphone, emergencycontactworkphone))
            conn.commit()
            close_conn()

            self.emergencycontact_entry.delete(0, tk.END)
            self.emergencycontactphone_entry.delete(0, tk.END)
            self.emergencycontactworkphone_entry.delete(0, tk.END)

            self.status_label.config(text="Emergency contact saved successfully.")
        except Exception as e:
            self.status_label.config(text=f"Error saving emergency contact: {e}")

class InsuranceForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Labels for the form fields
        insurancecompany_label = tk.Label(self, text="Insurance Company:")
        insuranceaddress_label = tk.Label(self, text="Insurance Address:")
        insurancecity_label = tk.Label(self, text="Insurance City:")
        insurancestate_label = tk.Label(self, text="Insurance State:")
        insurancepostalcode_label = tk.Label(self, text="Insurance Postal Code:")
        insurancecountry_label = tk.Label(self, text="Insurance Country:")
        policynumber_label = tk.Label(self, text="Policy Number:")
        expirydate_label = tk.Label(self, text="Expiry Date:")

        # Form fields
        self.insurancecompany_entry = tk.Entry(self)
        self.insuranceaddress_entry = tk.Entry(self)
        self.insurancecity_entry = tk.Entry(self)
        self.insurancestate_entry = tk.Entry(self)
        self.insurancepostalcode_entry = tk.Entry(self)
        self.insurancecountry_entry = tk.Entry(self)
        self.policynumber_entry = tk.Entry(self)
        self.expirydate_entry = tk.Entry(self)

        # Grid layout
        insurancecompany_label.grid(row=0, column=0)
        self.insurancecompany_entry.grid(row=0, column=1)
        insuranceaddress_label.grid(row=1, column=0)
        self.insuranceaddress_entry.grid(row=1, column=1)
        insurancecity_label.grid(row=2, column=0)
        self.insurancecity_entry.grid(row=2, column=1)
        insurancestate_label.grid(row=3, column=0)
        self.insurancestate_entry.grid(row=3, column=1)
        insurancepostalcode_label.grid(row=4, column=0)
        self.insurancepostalcode_entry.grid(row=4, column=1)
        insurancecountry_label.grid(row=5, column=0)
        self.insurancecountry_entry.grid(row=5, column=1)
        policynumber_label.grid(row=6, column=0)
        self.policynumber_entry.grid(row=6, column=1)
        expirydate_label.grid(row=7, column=0)
        self.expirydate_entry.grid(row=7, column=1)

        # Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_insurance)
        self.save_button.grid(row=8, column=1)

        # Status label
        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=9, column=1)

    def save_insurance(self, personid):
        try:
            insurancecompany = self.insurancecompany_entry.get()
            insuranceaddress = self.insuranceaddress_entry.get()
            insurancecity = self.insurancecity_entry.get()
            insurancestate = self.insurancestate_entry.get()
            insurancepostalcode = self.insurancepostalcode_entry.get()
            insurancecountry = self.insurancecountry_entry.get()
            policynumber = self.policynumber_entry.get()
            expirydate = self.expirydate_entry.get()

            # Save the insurance data to the database
            c.execute("INSERT INTO Insurance (personid, insurancecompany, insuranceaddress, insurancecity, insurancestate, insurancepostalcode, insurancecountry, policynumber, expirydate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  (personid, insurancecompany, insuranceaddress, insurancecity, insurancestate, insurancepostalcode, insurancecountry, policynumber, expirydate))

            conn.commit()
            close_conn()

            self.insurancecompany_entry.delete(0, tk.END)
            self.insuranceaddress_entry.delete(0, tk.END)
            self.insurancecity_entry.delete(0, tk.END)
            self.insurancestate_entry.delete(0, tk.END)
            self.insurancepostalcode_entry.delete(0, tk.END)
            self.insurancecountry_entry.delete(0, tk.END)
            self.policynumber_entry.delete(0, tk.END)
            self.expirydate_entry.delete(0, tk.END)

            self.status_label.config(text="Insurance information saved successfully.")
        except Exception as e:
            self.status_label.config(text=f"Error saving insurance information: {e}")

class MedicalHistoryForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Labels for the form fields
        hepatitisb_label = tk.Label(self, text="Hepatitis B:")
        chickenpox_label = tk.Label(self, text="Chickenpox:")
        measles_label = tk.Label(self, text="Measles:")
        significantmedicalhistory_label = tk.Label(self, text="Significant Medical History:")
        medicalproblems_label = tk.Label(self, text="Medical Problems:")
        medication_label = tk.Label(self, text="Medication:")
        allergies_label = tk.Label(self, text="Allergies:")

        # Form fields
        self.hepatitisb_var = tk.BooleanVar()
        self.hepatitisb_checkbutton = tk.Checkbutton(self, variable=self.hepatitisb_var)
        self.chickenpox_var = tk.BooleanVar()
        self.chickenpox_checkbutton = tk.Checkbutton(self, variable=self.chickenpox_var)
        self.measles_var = tk.BooleanVar()
        self.measles_checkbutton = tk.Checkbutton(self, variable=self.measles_var)
        self.significantmedicalhistory_text = tk.Text(self, height=3, width=30)
        self.medicalproblems_text = tk.Text(self, height=3, width=30)
        self.medication_text = tk.Text(self, height=2, width=30)
        self.allergies_text = tk.Text(self, height=2, width=30)

        # Grid layout
        hepatitisb_label.grid(row=0, column=0)
        self.hepatitisb_checkbutton.grid(row=0, column=1)
        chickenpox_label.grid(row=1, column=0)
        self.chickenpox_checkbutton.grid(row=1, column=1)
        measles_label.grid(row=2, column=0)
        self.measles_checkbutton.grid(row=2, column=1)
        significantmedicalhistory_label.grid(row=3, column=0)
        self.significantmedicalhistory_text.grid(row=3, column=1)
        medicalproblems_label.grid(row=4, column=0)
        self.medicalproblems_text.grid(row=4, column=1)
        medication_label.grid(row=5, column=0)
        self.medication_text.grid(row=5, column=1)
        allergies_label.grid(row=6, column=0)
        self.allergies_text.grid(row=6, column=1)

        # Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_medical_history)
        self.save_button.grid(row=7, column=1)

        # Status label
        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=8, column=1)

    def save_medical_history(self, personid):
        try:
            hepatitisb = self.hepatitisb_var.get()
            chickenpox = self.chickenpox_var.get()
            measles = self.measles_var.get()
            significantmedicalhistory = self.significantmedicalhistory_text.get("1.0", tk.END).strip()
            medicalproblems = self.medicalproblems_text.get("1.0", tk.END).strip()
            medication = self.medication_text.get("1.0", tk.END).strip()
            allergies = self.allergies_text.get("1.0", tk.END).strip()

            # Save the medical history data to the database
            c.execute("INSERT INTO MedicalHistory (personid, condition, diagnosis_date, treatment_start_date, treatment_end_date, notes, hepatitisb, chickenpox, measles, significantmedicalhistory, medicalproblems, medication, allergies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  (personid, hepatitisb, chickenpox, measles, significantmedicalhistory, medicalproblems, medication, allergies))

            conn.commit()
            
            self.hepatitisb_var.delete(0, tk.END) #*****
            self.hepatitisb_checkbutton.delete(0, tk.END) #*****
            self.measles_var.delete(0, tk.END) #*****
            self.significantmedicalhistory_text.delete(0, tk.END)
            self.medicalproblems_text.delete(0, tk.END)
            self.medication_text.delete(0, tk.END)
            self.allergies_text.delete(0, tk.END)

            self.status_label.config(text="Medical history saved successfully.")
        except Exception as e:
            self.status_label.config(text=f"Error saving medical history: {e}")

class RecordsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Create the table
        self.table = ttk.Treeview(self)
        self.table['columns'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.table.column('#0', width=100)
        self.table.column('1', width=100)
        self.table.column('2', width=100)
        self.table.column('3', width=100)
        self.table.column('4', width=100)
        self.table.column('5', width=100)
        self.table.column('6', width=100)
        self.table.column('7', width=100)
        self.table.column('8', width=100)
        self.table.column('9', width=100)
        self.table.heading('#0', text='Person ID')
        self.table.heading('1', text='First Name')
        self.table.heading('2', text='Last Name')
        self.table.heading('3', text='Phone Number')
        self.table.heading('4', text='Address')
        self.table.heading('5', text='City')
        self.table.heading('6', text='State')
        self.table.heading('7', text='Postal Code')
        self.table.heading('8', text='Country')
        self.table.heading('9', text='Birth Date')
        self.table.grid(row=0, column=0, sticky='nsew')

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.table.configure(yscrollcommand=scrollbar.set)

    def update_records(self, records):
        # Clear the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert the new records
        for record in records:
            self.table.insert('', 'end', text=record[0], values=record[1:])

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Form")

        # Create the form tabs
        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row=0, column=0, padx=10, pady=10)

        self.person_form = PersonForm(self.tabs)
        self.tabs.add(self.person_form, text="Person")

        self.emergency_contact_form = EmergencyContactForm(self.tabs)
        self.tabs.add(self.emergency_contact_form, text="Emergency Contact")

        self.insurance_form = InsuranceForm(self.tabs)
        self.tabs.add(self.insurance_form, text="Insurance")

        self.medical_history_form = MedicalHistoryForm(self.tabs)
        self.tabs.add(self.medical_history_form, text="Medical History")

        # Create the records view
        self.records_view = RecordsView(self)
        self.records_view.grid(row=1, column=0, padx=10, pady=10)

        # Load the saved records
        self.load_records()

    def load_records(self):
        # Fetch the records from the database
        records = self.fetch_records_from_db()
        if records is not None:
            self.records_view.update_records(records)
        else:
            # Handle the case where no records are found
            print("No records found in the database.")


    def fetch_records_from_db(self):
        try:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(
                host="78.38.35.219",
                port="5432",
                database="400463146",
                user="400463146",
                password="123456"
            )
            c = conn.cursor()

            # Fetch the records from the Person table
            c.execute("SELECT personid, firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate FROM Person")
            person_records = c.fetchall()

            # Close the database connection
            close_conn()

            return person_records
        except (Exception, psycopg2.Error) as error:
            print("Error fetching records from the database:", error)
            return None


def close_conn():
    conn.close()
    pass

# Implement CRUD operations
def create_person(firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate):
    c.execute("INSERT INTO Person (firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate))
    conn.commit()

def read_person(personid):
    c.execute("SELECT * FROM Person WHERE personid = %s", (personid,))
    return c.fetchone()

def update_person(personid, firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate):
    c.execute("UPDATE Person SET firstname = %s, lastname = %s, phonenumber = %s, address = %s, city = %s, state = %s, postalcode = %s, country = %s, birthdate = %s WHERE personid = %s", (firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate, personid))
    conn.commit()

def delete_person(personid):
    c.execute("DELETE FROM Person WHERE personid = %s", (personid,))
    conn.commit()

# Multi-table join query
def get_person_with_details(personid):
    c.execute("""SELECT p.firstname, p.lastname, p.phonenumber, p.address, p.city, p.state, p.postalcode, p.country, p.birthdate,
                        e.emergencycontact, e.emergencycontactphone, e.emergencycontactworkphone,
                        i.insurancecompany, i.insuranceaddress, i.insurancecity, i.insurancestate, i.insurancepostalcode, i.insurancecountry, i.policynumber, i.expirydate,
                        m.hepatitisb, m.chickenpox, m.measles, m.significantmedicalhistory, m.medicalproblems, m.medication, m.allergies
                 FROM Person p
                 LEFT JOIN EmergencyContact e ON p.personid = e.personid
                 LEFT JOIN Insurance i ON p.personid = i.personid
                 LEFT JOIN MedicalHistory m ON p.personid = m.personid
                 WHERE p.personid = %s""", (personid,))
    return c.fetchone()

# Data presentation
def get_person_count():
    c.execute("SELECT COUNT(*) FROM Person")
    return c.fetchone()[0]

def get_average_age():
    try:
        c.execute("SELECT AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, birthdate))) AS average_age FROM Person")
        result = c.fetchone()
        if result and result[0] is not None:
            return result[0]
        else:
            return 0.0
    except (psycopg2.Error, TypeError):
        return 0.0


def get_oldest_person():
    try:
        c.execute("SELECT firstname, lastname, birthdate FROM Person ORDER BY birthdate ASC LIMIT 1")
        result = c.fetchone()
        if result:
            return result
        else:
            return (None, None, None)
    except (psycopg2.Error, TypeError):
        return (None, None, None)


def get_youngest_person():
    try:
        c.execute("SELECT firstname, lastname, birthdate FROM Person ORDER BY birthdate DESC LIMIT 1")
        result = c.fetchone()
        if result:
            return result
        else:
            return (None, None, None)
    except (psycopg2.Error, TypeError):
        return (None, None, None)


# Create the main application window
# root = tk.Tk()
# root.title("Medform Database Management")

# # Create the person, emergency contact, insurance, and medical history forms
# person_form = PersonForm(root)
# person_form.grid(row=0, column=0)

# emergency_contact_form = EmergencyContactForm(root)
# emergency_contact_form.grid(row=0, column=1)

# insurance_form = InsuranceForm(root)
# insurance_form.grid(row=0, column=2)

# medical_history_form = MedicalHistoryForm(root)
# medical_history_form.grid(row=0, column=3)

# #**********************************************************************

# # firstname_entry = tk.Entry(root)
# # lastname_entry = tk.Entry(root)
# # birthdate_entry = tk.Entry(root)

# # firstname_entry.grid(row=0, column=1)
# # lastname_entry.grid(row=1, column=1)
# # birthdate_entry.grid(row=2, column=1)

# # def save_person():
# #     try:
# #         firstname = firstname_entry.get()
# #         lastname = lastname_entry.get()
# #         birthdate = birthdate_entry.get()

# #         c.execute("INSERT INTO Person (firstname, lastname, birthdate) VALUES (?, ?, ?)", (firstname, lastname, birthdate))
# #         conn.commit()

# #         firstname_entry.delete(0, tk.END)
# #         lastname_entry.delete(0, tk.END)
# #         birthdate_entry.delete(0, tk.END)

# #         status_label.config(text="Data saved successfully!", fg="green")
# #     except (psycopg2.Error) as e:
# #         status_label.config(text=f"Error saving data: {e}", fg="red")

# # status_label = tk.Label(root, text="")
# # status_label.grid(row=4, column=1)

# # save_button = tk.Button(root, text="Save", command=save_person)
# # save_button.grid(row=3, column=1)

# # root.mainloop()

# #*********************************************************************

# status_label = tk.Label(root, text="")
# status_label.grid(row=4, column=1)

# # Display aggregated information
# person_count = get_person_count()
# average_age = get_average_age()
# oldest_person = get_oldest_person()
# youngest_person = get_youngest_person()

# # Create labels to display the aggregated information
# person_count_label = Label(root, text=f"Total number of persons: {person_count}")
# person_count_label.grid(row=1, column=0)

# average_age_label = Label(root, text=f"Average age: {average_age:.2f} years")
# average_age_label.grid(row=2, column=0)

# if oldest_person[0] is not None and oldest_person[1] is not None and oldest_person[2] is not None:
#     oldest_person_label = Label(root, text=f"Oldest person: {oldest_person[0]} {oldest_person[1]} ({oldest_person[2]})")
#     oldest_person_label.grid(row=3, column=0)
# else:
#     oldest_person_label = Label(root, text="Unable to determine the oldest person")
#     oldest_person_label.grid(row=3, column=0)

# if youngest_person[0] is not None and youngest_person[1] is not None and youngest_person[2] is not None:
#     youngest_person_label = Label(root, text=f"Youngest person: {youngest_person[0]} {youngest_person[1]} ({youngest_person[2]})")
#     youngest_person_label.grid(row=4, column=0)
# else:
#     youngest_person_label = Label(root, text="Unable to determine the youngest person")
#     youngest_person_label.grid(row=4, column=0)

app = MainApplication()
app.mainloop()
# root.mainloop()