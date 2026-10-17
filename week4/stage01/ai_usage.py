
# AI-generated version from Part D (Microsoft Copilot)
appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

# Part F tests on the AI version
add_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")   # normal
add_appointment("", "Dr. John Doe", "2024-07-20 10:00 AM")              # blank name
add_appointment("Bob Johnson", "Dr. John Doe", "2024-07-20 10:00 AM")   # same doctor, same time
add_appointment(None, "Dr. John Doe", None)                            # None input

for appointment in appointments:
    print(appointment)

    appointments = []


    def add_appointment(patient_name, practitioner_name, appointment_time):
        appointment = {
            "patient": patient_name,
            "practitioner": practitioner_name,
            "time": appointment_time
        }
        appointments.append(appointment)


    # Example usage
    add_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")

    print(appointments)