class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self, patient_id, name, age, gender):
        if patient_id in self.patients:
            print(f"Patient with ID {patient_id} already exists.")
        else:
            self.patients[patient_id] = {"name": name, "age": age, "gender": gender}
            print(f"Patient with ID {patient_id} added successfully.")

    def add_doctor(self, doctor_id, name, specialty):
        if doctor_id in self.doctors:
            print(f"Doctor with ID {doctor_id} already exists.")
        else:
            self.doctors[doctor_id] = {"name": name, "specialty": specialty}
            print(f"Doctor with ID {doctor_id} added successfully.")

    def schedule_appointment(self, patient_id, doctor_id, date, time):
        if patient_id not in self.patients:
            print(f"Patient with ID {patient_id} not found.")
        elif doctor_id not in self.doctors:
            print(f"Doctor with ID {doctor_id} not found.")
        else:
            appointment_id = len(self.appointments) + 1
            self.appointments[appointment_id] = {"patient_id": patient_id, "doctor_id": doctor_id, "date": date, "time": time}
            print(f"Appointment scheduled successfully with ID {appointment_id}.")

    def cancel_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            print(f"Appointment with ID {appointment_id} cancelled successfully.")
        else:
            print("Appointment not found.")

    def display_appointments(self):
        if self.appointments:
            print("Appointments:")
            for appointment_id, appointment_info in self.appointments.items():
                print(f"ID: {appointment_id}, Patient ID: {appointment_info['patient_id']}, Doctor ID: {appointment_info['doctor_id']}, Date: {appointment_info['date']}, Time: {appointment_info['time']}")
        else:
            print("No appointments scheduled.")

# Example usage with user input
hospital_system = HospitalManagementSystem()

print("Welcome to the Hospital Management System!")

while True:
    print("\n1. Add Patient\n2. Add Doctor\n3. Schedule Appointment\n4. Cancel Appointment\n5. Display Appointments\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: ")
        hospital_system.add_patient(patient_id, name, age, gender)
    elif choice == '2':
        doctor_id = input("Enter doctor ID: ")
        name = input("Enter doctor name: ")
        specialty = input("Enter doctor specialty: ")
        hospital_system.add_doctor(doctor_id, name, specialty)
    elif choice == '3':
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        date = input("Enter appointment date: ")
        time = input("Enter appointment time: ")
        hospital_system.schedule_appointment(patient_id, doctor_id, date, time)
    elif choice == '4':
        appointment_id = int(input("Enter appointment ID to cancel: "))
        hospital_system.cancel_appointment(appointment_id)
    elif choice == '5':
        hospital_system.display_appointments()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
