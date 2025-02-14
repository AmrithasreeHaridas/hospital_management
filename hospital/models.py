from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)  # String field (max 100 characters)
    specialization = models.CharField(max_length=100)  # Specialization (e.g., Cardiologist)
    phone = models.CharField(max_length=15)  # Phone number field
    email = models.EmailField(unique=True)  # Email (must be unique)

    def __str__(self):
        return self.name  # Returns doctor's name when referenced
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()  # Integer field for age
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])  # Dropdown choices
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20, 
        choices=[("Scheduled", "Scheduled"), ("Completed", "Completed"), ("Cancelled", "Cancelled")], 
        default="Scheduled"
    )

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} on {self.date}"
