from appointment_class import Appointment
from patient_class import Patient
appointments = {}

def book():
    name = input("Enter the name of the patient: ").lower()
    age = int(input("Enter the age of the patient: "))
    disease = input("Enter the disease of the patient: ").lower()
    pat = Patient(name, age, disease)
    doc = input("Enter the doctor name: ")
    date = input("Enter the date of the appointment: ")
    appt = Appointment(pat, doc, date)
    appointments[name] = appt
    print(f"Appointment booked for {name}!")

def list_all():
    for x in appointments.values():
        print(x.get_summary())
def find():
    name_to_find = input("Enter the name of the patient to find the appointment details: ").lower()
    if name_to_find in appointments:
        return appointments[name_to_find].get_summary()
    return "No such patient exists."

def cancel():
    name_to_cancel = input("Enter the patient name to cancel the appointment: ").lower()
    if name_to_cancel in appointments:
        del appointments[name_to_cancel]
        return f"Patient {name_to_cancel}'s appointment is cancelled."
    return "No such patient exists"


is_on = True
while is_on:
    user_choice = input("book/cancel/list/find/quit: ").lower()
    if user_choice == "book":
        book()
    elif user_choice == "list":
        list_all()
    elif user_choice == "find":
        print(find())
    elif user_choice == "cancel":
        print(cancel())
    elif user_choice == "quit":
        is_on = False
