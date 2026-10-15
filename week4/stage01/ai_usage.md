appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

def show_appointments():
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )

add_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
add_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

show_appointments()