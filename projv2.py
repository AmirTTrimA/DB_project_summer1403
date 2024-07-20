import tkinter as tk
from tkinter import Frame, ttk, messagebox
from tkinter import Toplevel, Label, Entry, Button
import psycopg2

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
# (Assuming tables are already created as shown in your original code)

class PersonForm(Frame):
    def __init__(self, master, person_data):
        super().__init__(master)
        self.person_data = person_data
        self.create_widgets()

    def create_widgets(self):
        # Labels for the form fields
        labels = ["First Name:", "Last Name:", "Phone Number:", "Address:", "City:", "State:", "Postal Code:", "Country:", "Birthdate:"]
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self, text=label).grid(row=idx, column=0)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1)
            self.entries[label] = entry

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

class EmergencyContactForm(Frame):
    def __init__(self, master, person_data):
        super().__init__(master)
        self.person_data = person_data
        self.create_widgets()

    def create_widgets(self):
        labels = ["Emergency Contact:", "Emergency Contact Phone:", "Emergency Contact Work Phone:"]
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self, text=label).grid(row=idx, column=0)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1)
            self.entries[label] = entry

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

class InsuranceForm(Frame):
    def __init__(self, master, person_data):
        super().__init__(master)
        self.person_data = person_data
        self.create_widgets()

    def create_widgets(self):
        labels = ["Insurance Company:", "Insurance Address:", "Insurance City:", "Insurance State:", "Insurance Postal Code:", "Insurance Country:", "Policy Number:", "Expiry Date:"]
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self, text=label).grid(row=idx, column=0)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1)
            self.entries[label] = entry

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

class MedicalHistoryForm(Frame):
    def __init__(self, master, person_data):
        super().__init__(master)
        self.person_data = person_data
        self.create_widgets()

    def create_widgets(self):
        labels = ["Hepatitis B:", "Chickenpox:", "Measles:", "Significant Medical History:", "Medical Problems:", "Medication:", "Allergies:"]
        self.entries = {}
        self.check_vars = {}

        for idx, label in enumerate(labels):
            if label in ["Hepatitis B:", "Chickenpox:", "Measles:"]:
                var = tk.BooleanVar(value=False)  # Set default value to False
                checkbutton = tk.Checkbutton(self, text=label, variable=var)
                checkbutton.grid(row=idx, column=0, sticky='w')
                self.check_vars[label] = var
            else:
                tk.Label(self, text=label).grid(row=idx, column=0)
                text = tk.Text(self, height=2, width=30)
                text.grid(row=idx, column=1)
                self.entries[label] = text

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete("1.0", tk.END)
        for var in self.check_vars.values():
            var.set(False)  # Reset checkboxes to unchecked

class RecordsView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.table = ttk.Treeview(self, columns=('ID', 'First Name', 'Last Name', 'Phone', 'Address', 'City', 'State', 'Postal Code', 'Country', 'Birthdate'), show='headings')

        # Set up column headings and widths
        self.table.heading('ID', text='ID')
        self.table.column('ID', width=50, anchor='center')

        self.table.heading('First Name', text='First Name')
        self.table.column('First Name', width=100, anchor='center')

        self.table.heading('Last Name', text='Last Name')
        self.table.column('Last Name', width=100, anchor='center')

        self.table.heading('Phone', text='Phone')
        self.table.column('Phone', width=100, anchor='center')

        self.table.heading('Address', text='Address')
        self.table.column('Address', width=150, anchor='center')

        self.table.heading('City', text='City')
        self.table.column('City', width=100, anchor='center')

        self.table.heading('State', text='State')
        self.table.column('State', width=100, anchor='center')

        self.table.heading('Postal Code', text='Postal Code')
        self.table.column('Postal Code', width=100, anchor='center')

        self.table.heading('Country', text='Country')
        self.table.column('Country', width=100, anchor='center')

        self.table.heading('Birthdate', text='Birthdate')
        self.table.column('Birthdate', width=100, anchor='center')

        self.table.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_records(self):
        try:
            c.execute("SELECT personid, firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate FROM Person")
            records = c.fetchall()
            # print("Fetched records:", records)  # Debugging line
            self.update_records(records)
        except Exception as e:
            print("Error loading records:", e)

    def update_records(self, records):
        # print("Updating records in Treeview")  # Debugging line
        for item in self.table.get_children():
            self.table.delete(item)
        for record in records:
            # print("Inserting record:", record)  # Debugging line
            self.table.insert('', 'end', values=record)  # Insert new records



    def view_details(self):
        person_id = self.id_entry.get()
        if not person_id.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid Person ID.")
            return

        try:
            c.execute("SELECT * FROM Person WHERE personid = %s", (person_id,))
            person = c.fetchone()
            if person:
                self.show_person_details(person)
            else:
                messagebox.showinfo("Not Found", "No person found with that ID.")
        except Exception as e:
            print("Error fetching details:", e)

    def show_person_details(self, person):
        details_window = tk.Toplevel(self)
        details_window.title("Person Details")

        labels = ["Person ID", "First Name", "Last Name", "Phone Number", "Address", "City", "State", "Postal Code", "Country", "Birthdate"]
        
        for idx, label in enumerate(labels):
            tk.Label(details_window, text=label + ":").grid(row=idx, column=0, sticky='w')
            tk.Label(details_window, text=person[idx]).grid(row=idx, column=1, sticky='w')

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Form")

        # Temporary storage for person data
        self.person_data = {}

        # Create the form tabs
        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row=0, column=0, padx=10, pady=10)

        self.person_form = PersonForm(self.tabs, self.person_data)
        self.tabs.add(self.person_form, text="Person")

        self.emergency_contact_form = EmergencyContactForm(self.tabs, self.person_data)
        self.tabs.add(self.emergency_contact_form, text="Emergency Contact")

        self.insurance_form = InsuranceForm(self.tabs, self.person_data)
        self.tabs.add(self.insurance_form, text="Insurance")

        self.medical_history_form = MedicalHistoryForm(self.tabs, self.person_data)
        self.tabs.add(self.medical_history_form, text="Medical History")

        # Save button for all tabs
        self.save_button = tk.Button(self, text="Save All", command=self.save_all)
        self.save_button.grid(row=1, column=0, padx=10, pady=10)

        # Records view button
        self.records_button = tk.Button(self, text="View Records", command=self.open_records_view)
        self.records_button.grid(row=2, column=0, padx=10, pady=10)

        # Entry for Person ID
        self.person_id_label = Label(self, text="Enter Person ID:")
        self.person_id_label.grid(row=3, column=0, padx=10, pady=5)

        self.person_id_entry = Entry(self)
        self.person_id_entry.grid(row=4, column=0, padx=10, pady=5)

        self.fetch_button = Button(self, text="Fetch Info", command=self.fetch_person_info)
        self.fetch_button.grid(row=5, column=0, padx=10, pady=5)

    def open_records_view(self):
        records_window = tk.Toplevel(self)
        records_window.title("Records View")
        records_view = RecordsView(records_window)
        records_view.pack(fill=tk.BOTH, expand=True)  # Ensure the frame is packed
        records_view.load_records()  # Load records immediately after creating the view

    def fetch_person_info(self):
        person_id = self.person_id_entry.get()
        if person_id:
            try:
                # Fetch all relevant data using JOIN
                query = """
                SELECT p.*, ec.emergencycontact, ec.emergencycontactphone, ec.emergencycontactworkphone,
                    i.insurancecompany, i.insuranceaddress, i.insurancecity, i.insurancestate,
                    i.insurancepostalcode, i.insurancecountry, i.policynumber, i.expirydate,
                    mh.hepatitisb, mh.chickenpox, mh.measles, mh.significantmedicalhistory,
                    mh.medicalproblems, mh.medication, mh.allergies
                FROM Person p
                LEFT JOIN EmergencyContact ec ON p.personid = ec.personid
                LEFT JOIN Insurance i ON p.personid = i.personid
                LEFT JOIN MedicalHistory mh ON p.personid = mh.personid
                WHERE p.personid = %s
                """
                c.execute(query, (person_id,))
                record = c.fetchone()
                if record:
                    self.show_person_info(record)
                else:
                    print("No record found for this Person ID.")
            except Exception as e:
                print("Error fetching person info:", e)

    def show_person_info(self, record):
        info_window = Toplevel(self)
        info_window.title("Person Information")

        # Create a Treeview widget
        tree = ttk.Treeview(info_window, columns=("Field", "Value"), show='headings')
        tree.heading("Field", text="Field")
        tree.heading("Value", text="Value")

        # Set column widths
        tree.column("Field", width=150)
        tree.column("Value", width=300)

        # Insert data into the Treeview
        fields = [
            'Person ID', 'First Name', 'Last Name', 'Phone', 'Address', 'City', 
            'State', 'Postal Code', 'Country', 'Birthdate', 'Emergency Contact', 
            'Emergency Contact Phone', 'Emergency Contact Work Phone', 
            'Insurance Company', 'Insurance Address', 'Insurance City', 
            'Insurance State', 'Insurance Postal Code', 'Insurance Country', 
            'Policy Number', 'Expiry Date', 'Hepatitis B', 'Chickenpox', 
            'Measles', 'Significant Medical History', 'Medical Problems', 
            'Medication', 'Allergies'
        ]

        for field, value in zip(fields, record):
            tree.insert("", "end", values=(field, value))

        # Pack the Treeview into the window
        tree.pack(fill=tk.BOTH, expand=True)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(info_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)



    def save_all(self):
        try:
            # Collect data from all tabs
            self.person_data['firstname'] = self.person_form.entries["First Name:"].get()
            self.person_data['lastname'] = self.person_form.entries["Last Name:"].get()
            self.person_data['phonenumber'] = self.person_form.entries["Phone Number:"].get()
            self.person_data['address'] = self.person_form.entries["Address:"].get()
            self.person_data['city'] = self.person_form.entries["City:"].get()
            self.person_data['state'] = self.person_form.entries["State:"].get()
            self.person_data['postalcode'] = self.person_form.entries["Postal Code:"].get()
            self.person_data['country'] = self.person_form.entries["Country:"].get()
            self.person_data['birthdate'] = self.person_form.entries["Birthdate:"].get()

            self.person_data['emergency_contact'] = self.emergency_contact_form.entries["Emergency Contact:"].get()
            self.person_data['emergency_contact_phone'] = self.emergency_contact_form.entries["Emergency Contact Phone:"].get()
            self.person_data['emergency_contact_workphone'] = self.emergency_contact_form.entries["Emergency Contact Work Phone:"].get()

            self.person_data['insurance_company'] = self.insurance_form.entries["Insurance Company:"].get()
            self.person_data['insurance_address'] = self.insurance_form.entries["Insurance Address:"].get()
            self.person_data['insurance_city'] = self.insurance_form.entries["Insurance City:"].get()
            self.person_data['insurance_state'] = self.insurance_form.entries["Insurance State:"].get()
            self.person_data['insurance_postalcode'] = self.insurance_form.entries["Insurance Postal Code:"].get()
            self.person_data['insurance_country'] = self.insurance_form.entries["Insurance Country:"].get()
            self.person_data['policy_number'] = self.insurance_form.entries["Policy Number:"].get()
            self.person_data['expiry_date'] = self.insurance_form.entries["Expiry Date:"].get()

            self.person_data['hepatitisb'] = self.medical_history_form.check_vars["Hepatitis B:"].get()
            self.person_data['chickenpox'] = self.medical_history_form.check_vars["Chickenpox:"].get()
            self.person_data['measles'] = self.medical_history_form.check_vars["Measles:"].get()
            self.person_data['significant_medical_history'] = self.medical_history_form.entries["Significant Medical History:"].get("1.0", tk.END).strip()
            self.person_data['medical_problems'] = self.medical_history_form.entries["Medical Problems:"].get("1.0", tk.END).strip()
            self.person_data['medication'] = self.medical_history_form.entries["Medication:"].get("1.0", tk.END).strip()
            self.person_data['allergies'] = self.medical_history_form.entries["Allergies:"].get("1.0", tk.END).strip()

            # Validate that all required fields are filled
            if not all(self.person_data.values()):
                raise ValueError("All fields must be filled out.")

            # Insert data into the database
            self.insert_data_into_db()

            # Clear entries after successful save
            self.clear_entries()

        except Exception as e:
            print(f"Error saving data: {e}")

    def insert_data_into_db(self):
        # Insert person data
        c.execute("INSERT INTO Person (firstname, lastname, phonenumber, address, city, state, postalcode, country, birthdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING personid", 
                  (self.person_data['firstname'], self.person_data['lastname'], self.person_data['phonenumber'], self.person_data['address'], self.person_data['city'], self.person_data['state'], self.person_data['postalcode'], self.person_data['country'], self.person_data['birthdate']))
        personid = c.fetchone()[0]
        conn.commit()

        # Insert emergency contact data
        c.execute("INSERT INTO EmergencyContact (personid, emergencycontact, emergencycontactphone, emergencycontactworkphone) VALUES (%s, %s, %s, %s)", 
                  (personid, self.person_data['emergency_contact'], self.person_data['emergency_contact_phone'], self.person_data['emergency_contact_workphone']))
        conn.commit()

        # Insert insurance data
        c.execute("INSERT INTO Insurance (personid, insurancecompany, insuranceaddress, insurancecity, insurancestate, insurancepostalcode, insurancecountry, policynumber, expirydate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  (personid, self.person_data['insurance_company'], self.person_data['insurance_address'], self.person_data['insurance_city'], self.person_data['insurance_state'], self.person_data['insurance_postalcode'], self.person_data['insurance_country'], self.person_data['policy_number'], self.person_data['expiry_date']))
        conn.commit()

        # Insert medical history data
        c.execute("INSERT INTO MedicalHistory (personid, hepatitisb, chickenpox, measles, significantmedicalhistory, medicalproblems, medication, allergies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                  (personid, self.person_data['hepatitisb'], self.person_data['chickenpox'], self.person_data['measles'], self.person_data['significant_medical_history'], self.person_data['medical_problems'], self.person_data['medication'], self.person_data['allergies']))
        conn.commit()

    def clear_entries(self):
        self.person_form.clear_entries()
        self.emergency_contact_form.clear_entries()
        self.insurance_form.clear_entries()
        self.medical_history_form.clear_entries()


def close_conn():
    conn.close()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
    close_conn()
