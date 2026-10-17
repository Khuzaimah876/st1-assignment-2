# WEEK 5
### Activity 1 stakeholder

Problem and Scope:

Smartcare currently uses spreadsheets and records on paper,
 Due to this problems that arise are duplicate bookings,
 difficulty locating patient records,
 inconsistent appointment status information.
 The system will manage patient bookings, how practioners view schedules and how recptionists find patient bookings on the system.

#### 2. Stakeholder

| Stakeholder | Need                                                                           | Evidence                                                                                                                                                              |
| :--- |:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Receptionist | Book appointments, reschudle appointments, and search for patient information. | Staff currently use spreadsheets and manually record information. This leads to duplicate bookings and missing pateint records.                                       |
|Practitioner | View daily booking schedule and patient record history                         |  
| Management | To oversee bookings and to ensure the maintanence of the clinic | Management requested for a simple system that isnt a complex hospital information system, that will replace the current fragmented manual spreadsheet system. | 
| Patient | To have their bookings corrcetly scheduled, by allowing the pateints to view their booking details. | Poor record keeping affects patient appointments and patient record. 


# Functional requirements

Fr-01: System creates record,

Fr-02: System searches for a patient using id

Fr-03: System will create an appointment that can be viewed by the medical team.

Fr-04: System needs to prevent duplicate bookings by checking the practitioners availability before confirming a time slot. 

Fr-05: System needs to allow the reception team to be able to cancel, update or modify bookings.

Fr-06: System needs to allow staff to be able to cancel a booking while retaining the cancellation status instead of removing it.

Fr-07: System needs to provide the practitioner with their daily and weekly appointment schedule.

Fr-08: System needs to allow staff to record and update bookings consistently, progressing in different stages (e.g, Booked, cancelled, completed)

Fr-09: System needs to allow management to view reports on appointment bookings.  #changed: management to view appointment bookings. 

Fr-10: System needs to store patient consultation history to prevent lost information 

Fr-11: System needs to allow patients to filter appointments based on time, date and practitioner or booking status. 

Fr-12: System needs to be able to restrict or lock patient data for privacy purposes based on roles, so health records can only be viewed by practitioners, not receptionist, management or any other patient. 

# Non functional requirements
NFR-01: System code must be clear and conscise, so regular updates and patch fixes can be released and made by smaller teams. 

NFR-02: System shall allow the staff members to view the patient records and appointment bookings within 2 to 3 seconds.

NFR-03: The system should be able to reliably store information without loosing any patient records or sensitive information. 

NFR-04: The system needs to maintain integrity by validating all appointments to prevent overlapping schedules. 

NFR-05: The system should keep the information of patients, practitioners and appointments when the application is closed and reopened.  

NFR-06: System requires a login from staff to view patient medical history and other sensitive information.

# User stories
US-01: As a receptionist, I want to book appointments without creating duplicates, so that the clinic schedule stays accurate and reliable

US-02: As a receptionist, I want to search for existing patient records instantly by ID or name, so that I don't waste time looking through spreadsheets and paper records.

US-03: As a practitioner, I want to view my daily appointment schedule and patient history, so that I am fully prepared for consultations without visibility issues.

US-04: As a clinic manager, I want to view consistent and up-to-date appointment statuses, so that I can track clinic operations properly.

US-05: As a patient, I want my appointment details and medical history to be accurately recorded, so that there are no mix-ups or lost records during my visit.

US-06: As a receptionist, I want to update or cancel an appointment and keep a permanent record of it, so that we maintain a clear appointment history.


# Acceptance Criteria


| Acceptance criteria                                        | Given                                                                                                     | When                                                               | Then                                                                                                                       |
|:-----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Patient search                                             | Given patient history exists in the system                                                                | When any staff member searches for the name in the system using id | System must display the correct information                                                                                |
| Create an appointment                                      | Given patient record exists and a practitioner is available                                               | When a recpetionist or any staff member clicks create appointment  | Appointment and booking details must be succesfully logged and stored in the system                                        |
| Practitioner availability                                  | Given current logged availability of the practitioner                                                     | When viewed by a receptionist, staff member or practitioner        | System must display all availalble appointment and booking times                                                           |
| Cancel appointment                                         | Given that a currect existing booking exists for this patient                                             | When a recpetionist cancels a booking                              | Then the booking status for appointment should change to cancelled in system and the record should be kept in the history. |     
| Prevent double booking <br/>(negative or failing scenario) | Given the practitioner is booked for a specific time slot                                                 | When a receptionist or staff member tries to book within that time slot | Then the system should display an error message and reject the request of the staff member to double book.                 |

# Part g) Verify the ai Review

| AI suggestion                                                          | Evidence?                                                                                                                                            | Decision   | Reason                                                               | Verification                                                                                                                                                                             |
|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Make the appointment statuses clearer (FR-08)                          | Mentioned in the assignment 2 sheet  "inconsistent appointment status information", the clinic already has messy and inconsistent status information | Modified   | The terms in FR-08 are vague such as completed, booked and cancelled | Change the three to cancelled and completed only, the "booked" doesnt make sense because for the patient to be in this record implies they would have booked and appointment previously. |
| Make the reports clear (FR-09)                                         | Ai said the word "report" was unclear                                                                                                                | Modified   | The word report was vague and was confusing                          | removed modified word                                                                                                                                                                    |
| Keep cancelled bookings in a backup, don't remove them  or delete them | Yes, mentioned in the assignment 2 sheet "lack of reliable appointment history"                                                                      | Accepted   | Matches the case in the assignment 2 sheet                           | covered by FR-06                                                                                                                                                                         |




