from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm

def home(request):
    return render(request, 'hospital/home.html')
def doctor_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointment_list.html', {'appointments': appointments})
def book_appointment(request):
    if request.method == "POST":  # If form is submitted
        form = AppointmentForm(request.POST)
        if form.is_valid():  # Validate form
            form.save()  # Save to database
            return redirect('appointment_list')  # Redirect to appointment list
    else:
        form = AppointmentForm()
    return render(request, 'hospital/book_appointment.html', {'form': form})

