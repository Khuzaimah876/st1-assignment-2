Based on the code in Part B from Stage_1_Lab_Student_Handout (1), here is a response you can use for Part C and Part D.

Part C - Use AI as Tutor
1. What the code does

The program creates a simple appointment-booking system for SmartCare. It:

Stores appointments in a list called appointments.
Uses the book_appointment() function to create an appointment record.
Stores each appointment as a dictionary containing:
patient name
practitioner name
appointment time
Adds each appointment to the appointments list.
Uses display_appointments() to print all recorded appointments.
Checks that the patient name is not empty before creating an appointment.
2. Three limitations

Only the patient name is validated

Practitioner name and appointment time could be blank or invalid.

No duplicate appointment checking

Two appointments could be booked for the same practitioner at the same time.

Data is not saved permanently

When the program stops, all appointment information is lost because it is only stored in memory.
3. Suggested improvements
Validate practitioner names and appointment times.
Check for appointment conflicts before adding a new booking.
Add error handling for unusual inputs such as None.
Allow users to enter appointment details through keyboard input.
Save appointments to a file for future use.
4. (No full rewrite provided)

As requested, these are suggestions only and not a complete replacement application.

5. Questions to test your understanding
Why is a dictionary a useful way to store appointment information instead of using three separate variables?
What would happen if book_appointment("", "Dr. Smith", "10:00 AM") was executed, and why?


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


#for part G) An issue in the code is the double booking so using AI to fix as part c ai is on,

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    for existing in appointments:
        if existing["practitioner"] == practitioner_name and existing["time"] == appointment_time:
            raise ValueError("This practitioner is already booked at that time")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

