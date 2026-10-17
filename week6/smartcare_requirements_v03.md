# Week 6 Stage 3 lab report

### Part A. Requirements Review
#### Task: Highlight nouns, verbs and buisness rules in smartcare v02.

##### Nouns: 
Patient, Staff, Medical practitioner, patient record, management, appointment, appointment status, medical practitioner record

##### Verb: 
Create, upload, search, prevent, book, log in, oversee, provide, manage, lookup, update, search, prevent, book, log in, preserve, maintain, display.

##### Buisness rules:
Fr-04: To prevent double bookings, The system should check the desired practitioner's schedule and availability before confirming an appointment spot. (Practitioner cant have 2 bookings at the same time).


Fr-06: The system must not erase cancellation history when staff cancel a booking.

FR-12: The system needs to be able to lock patient records so authorised personel can view sensititive medical history. 


##### Candidate classes

| Candiate     | Requirement                                                                   | Attributes                                                  | Function       |
|:-------------|:------------------------------------------------------------------------------|:------------------------------------------------------------|----------------|
| Patient      | Fr-01: System creates record and Fr-02 : System searches for patient using id | PatientID, name, ContactDetails, CreateRecord               | getPatientID() |
| Practitioner | Fr-01 and Fr-07                                                               | practitionerID, name, schedule                              | ViewSchedule(), getPractitionerID()
| Appointment  | Fr-01, Fr-03, Fr-04, Fr-05, Fr-06, Fr-08, Fr-09, Fr-10, Fr-12                 | AppointmentID, Status                                       | bookAppointment(), cancelAppointment(), updateStatus() 

##### CRC cards

| Class name   | Responsibility                                                                                                                          | Collaborators                   | 
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| Patient      | Store patient details and provide when requested                                                                                        | The collaborator is Appointment | 
| Practitioner | Store practitioner schedule and display upcoming appointments. Show patient ID                                                          | Appointment                     | 
| Appointment  | Store the date, time and information for patient booking, refuse double booking (booking two patients same time with same practitioner) | Patient and Practitioner        |

##### UML design 
Patient:
PatientID: String
name: string
contactDetails: string

Practitioner: 
practitionerID: string
name: string
schedule: string

Appointment:
appointmentID: string
status: string


##### AI Design review

Core Concept: PatientSuggested Attributes: patientID, firstName, lastName, phoneContact, medicalNotesSupporting Evidence: Linked directly to profile creation and search capabilities (FR-01, FR-02)

and record preservation (FR-10).   Relationship Rule: Associated with zero or many (0..*) appointments, ensuring historical tracking.Core Concept: PractitionerSuggested Attributes: practitionerID, doctorName, medicalSpecialty, availabilityStatusSupporting Evidence: Tied to staff and practitioner record management (FR-01) and schedule visibility (FR-07).   Relationship Rule: Can be linked to multiple (0..*) appointments throughout the clinic day.Core Concept: AppointmentSuggested Attributes: appointmentID, scheduledDateTime, currentStatus (Booked, Cancelled, Completed)Supporting Evidence: Derived from appointment creation rules (FR-03), duplicate prevention checks (FR-04), cancellation history retention (FR-06), and status updates (FR-08).   Relationship Rule: Acts as the central association bridge, requiring exactly one (1) Patient and exactly one (1) Practitioner per booking instance.


## Compare and decide: 
##### Accepted:
We can accept the current status as this is the same as FR-08 

##### Modified: 
The AI suggested an availabilityStatus attribute on Practitioner (FR-07). I changed this to "is_available(date_time)", because one stored value is not enough to provide information on a practitioner being free at various times. 
Availability must be solved from the appointments not from the has to be worked out from their appointments. This is how the double booking problem gets checked (FR-04)

##### Rejected: 
The AI suggested a medicalSpecialty attribute for the Practitioner. No requirement that was created mentions medicalSpeciality this, ontop of this and the case study only mentions GPs, so it is over-design for a simple clinic system.

## Python skeleton:
The Python skeleton is made from the UML that was created not to long ago. 

Patient: 
def __init__(self, patient_id, name, contact_details):

        self.patient_id = patient_id            # Unique patient ID used for searching (FR-02)
        self.name = name
        self.contact_details = contact_details
        self.appointments = []

Practitioner: def __init__(self, practitioner_id, name):

        self.practitioner_id = practitioner_id   #Practitioner id added to differented between different practitioners.
        self.name = name
        self.appointments = [] 

Appointment: def __init__(self, appointment_id, patient, practitioner, date_time):

        self.appointment_id = appointment_id     #appointment id allows the system to recognise the appointment and tell them apart from other appointments.
        self.patient = patient                  
        self.practitioner = practitioner        
        self.date_time = date_time              
        self.status = "Booked"

### H) 
Every class and attribute and method in the UML above appears in the code with the same name, and the code doesn't add anything extra that isn't mentioned in the UML. 



### Reflection

The hardest modelling decision was finding the most appropriate classes and determining how they should relate to each other based on the SmartCare requirements. From my requirements analysis, I identified Patient, Practitioner, and Appointment as the candidate classes and linked them to the functional requirements from week 5. The AI did something similar as it also identified Patient, Practitioner, and Appointment as the classes. This gave me reassurance  that my modelling decisions were reasonable and supported by the requirements as ai was also on the same page.
However with that said the main difference between my model and the AI model was the level of detail. The AI produced extra attributes such as firstName, lastName, phoneContact, medicalNotes, medicalSpecialty, and availabilityStatus. The AI also used a more formal method of writing out the relationships between classes using UML notation as follows, “Practitioner (1) ---- (0..*)”, this however wasn't mentioned to us in the design specifications so it is something the ai has added on its own.
The evidence supporting my choices came from the functional requirements. FR-01 and FR-02 supported the “Patient” class, FR-07 supported the Practitioner class, and FR-03, FR-04, FR-05, FR-06, FR-08, FR-09, FR-10, and FR-12 supported the Appointment class. Utilizing requirement IDs makes sure that my UML and CRC design decisions were linked to stakeholder/client requirements instead of assumptions.













