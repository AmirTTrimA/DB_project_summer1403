import tkinter as tk
from tkinter import ttk
import psycopg2

from proj import PersonForm, EmergencyContactForm, InsuranceForm, MedicalHistoryForm, RecordsView

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
        self.records_view.update_records(records)

    def fetch_records_from_db(self):
        conn = psycopg2.connect(
            host="78.38.35.219",
            port="5432",
            database="400463146",
            user="400463146",
            password="123456"
        )
        c = conn.cursor()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
