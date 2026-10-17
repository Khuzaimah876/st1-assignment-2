# Limitations, comparison and verification

### Limitations:

From the human code there are a few limitations that can be seen. For example, 
1. There is no cancel booking button.
2. There is no prevention in the code against double booking, a double booking can occur by either two patients booked at the exact same time or 2 pateints booked with the same medical practitioner at the same time. 
3. New patient details cannot be added, as this software is replacing the manual spreadsheet, there should be an option to add a new patient to the system. 
4. There is no storage or previous history which shows the patient's previous record in terms of visiting the clinic. 
5. from the code, only the patient name is checked, the practitioner and time for appointment can be blank and it doesnt affect the application.

### Comparison

| Question           | Human version | AI Version                                                     |
|:-------------------|:--------------|:---------------------------------------------------------------|
| Easy to understand | Yes           | Alot shorter and smaller than the human one, much more concise |
|Runs successfully? | Yes | Yes
| Uses only required features | Yes | Yes, followed the instructions well, no gui or anything out of the ds was created.
| Adds Assumptions | No | It assumes all the input is valid 
| Handles errors? | Partly, it accepts double booking but rejects no name | Assumes everything works 
| Could i explain it?  | Yes  | Yes | 



### Verification


| Test                                                             | Human version                                                                                                                      | AI Version   |
|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:-------------|
| Normal appointment                                               | Accepted                                                                                                                           | Yes accepted |
| Blank patient name                                               | Rejected with a value error message                                                                                                | Accepted     
| Two appointments for the same practitioner/time (double booking) | Accepted                                                                                                                           | Accepted     |  
| Strange input such as patient_name=None or appointment_time=None | Human code rejected the patient that had no name giving a value error message while the system accpeted with no time given.  | Accpeted     |

