# Part F) AI Requirements Review
1. Ambiguity
Requirement: FR-08

Requirement: System needs to allow staff to record and update bookings consistently, progressing in different stages (e.g., Booked, Cancelled, Completed).

Review: The requirement introduces booking stages but does not define all valid statuses or the rules for moving between them. For example, can a "Completed" booking be changed back to "Booked"?

Classification: Question requiring validation.

Requirement: FR-09

Requirement: System needs to allow management to view reports on appointment bookings.

Review: The term "reports" is unclear. The requirement does not specify whether reports should include appointment counts, cancellations, practitioner workload, patient history, or other information.

Classification: Question requiring validation.

2. Inconsistency
Requirement: FR-05 and FR-06

Review: FR-05 states that reception staff can cancel, update, or modify bookings, while FR-06 states that cancelled bookings must be retained rather than removed. These requirements are not contradictory, but the design must ensure that cancellation changes a booking's status instead of deleting the booking record.

Classification: Based on evidence.

3. Missing Clarification Questions
Question 1

What information should be included in a patient record created under FR-01?

Classification: Question requiring validation.

Question 2

What information should be included in management reports under FR-09?

Classification: Question requiring validation.

Question 3

How long should patient consultation history be retained under FR-10?

Classification: Question requiring validation.

Question 4

What staff roles are permitted to access patient information under FR-12 and NFR-06?

Classification: Question requiring validation.

4. Testability
Requirement: FR-04

Requirement: Prevent duplicate bookings by checking practitioner availability.

Review: This is testable. A tester can attempt to create two appointments with the same practitioner at the same time and verify that the second booking is rejected.

Classification: Based on evidence.

Requirement: FR-06

Requirement: Cancel a booking while retaining the cancellation status.

Review: This is testable. A tester can cancel an appointment and verify that the appointment record remains stored with a status of "Cancelled."

Classification: Based on evidence.

Requirement: NFR-02

Requirement: Staff members must be able to view patient records and appointments within 2 to 3 seconds.

Review: This is testable because response times can be measured and compared against the stated requirement.

Classification: Based on evidence.

Requirement: NFR-01

Requirement: System code must be easy and simple to understand and read.

Review: This requirement is difficult to measure objectively because "easy" and "simple" can be interpreted differently by different developers. Additional acceptance criteria would improve testability.

Classification: Question requiring validation.

Summary

Most requirements are clear and support the SmartCare system's main functions, including patient management, appointment booking, scheduling, reporting, and privacy controls. The strongest requirements are FR-04, FR-06, NFR-02, and NFR-05 because they can be tested objectively. Further clarification is needed for booking statuses (FR-08), management reports (FR-09), patient record content (FR-01), and access permissions (FR-12/NFR-06). Any future design decisions should be based on these confirmed requirements and not on assumptions.