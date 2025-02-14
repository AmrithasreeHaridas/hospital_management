import os
import django
from datetime import date, timedelta
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management.settings')
django.setup()

from hospital.models import Doctor, Patient, Appointment

# Sample data for Doctors
doctors_data = [
    {"name": "Dr. Robert Brown", "specialization": "Orthopedic", "phone": "9856789012", "email": "robertbrown@example.com"},
    {"name": "Dr. Sarah Lee", "specialization": "Pediatrician", "phone": "9812345678", "email": "sarahlee@example.com"},
    {"name": "Dr. David Wilson", "specialization": "Dermatologist", "phone": "9870987654", "email": "davidwilson@example.com"},
]

# Sample data for Patients
patients_data = [
    {"name": "Alice Johnson", "age": 30, "gender": "Female", "phone": "9823456789", "email": "alice@example.com"},
    {"name": "Bob Martin", "age": 45, "gender": "Male", "phone": "9812345678", "email": "bob@example.com"},
    {"name": "Charlie Brown", "age": 25, "gender": "Male", "phone": "9809876543", "email": "charlie@example.com"},
    {"name": "Diana Prince", "age": 40, "gender": "Female", "phone": "9786543210", "email": "diana@example.com"},
    {"name": "Ethan Hunt", "age": 35, "gender": "Male", "phone": "9754321987", "email": "ethan@example.com"},
]

# Insert doctors into the database
for doctor in doctors_data:
    Doctor.objects.create(**doctor)

# Insert patients into the database
for patient in patients_data:
    Patient.objects.create(**patient)

# Get all doctors and patients from the database
doctors = list(Doctor.objects.all())
patients = list(Patient.objects.all())

# Sample data for Appointments
appointments_data = []
for i in range(10):  # Creating 10 random appointments
    appointment = {
        "doctor": random.choice(doctors),  # Assign a random doctor
        "patient": random.choice(patients),  # Assign a random patient
        "date": date.today() + timedelta(days=random.randint(1, 30)),  # Random future date
        "time": f"{random.randint(9, 17)}:00",  # Random hour between 9 AM - 5 PM
        "status": random.choice(["Scheduled", "Completed", "Cancelled"]),
    }
    appointments_data.append(appointment)

# Insert appointments into the database
for appointment in appointments_data:
    Appointment.objects.create(**appointment)

print("✅ Sample data inserted successfully!")
