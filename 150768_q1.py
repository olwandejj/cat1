
def addPatient(patients):
    name = input("Enter the patient's name: ")
    age = input("Enter the patient's age: ")
    illness = input("Enter the patient's illness: ")
    patient = {
                'name': name, 
                'age': age, 
                'illness': illness
              }
    patients.append(patient)
    print(f"The patient named {name} has been successfully added.")


def showPatients(patients):
    if not patients:
        print("No patients were found.")
    else:
        for patient in patients:
            print(f"Name: {patient['name']}, \nAge: {patient['age']}, \nIllness: {patient['illness']}")


def searchPatient(patients):
    name = input("Enter the patient's name: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Name: {patient['name']}, \nAge: {patient['age']}, \nIllness: {patient['illness']}")
            return
    print(f"The patient named {name} was not found.")


def removePatient(patients):
    name = input("Enter the patient's name: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"The patient named {name} was successfully removed.")
            return
    print(f"The patient named {name} was not found.")


def main():
    patients = []
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        choice = input("Choose an option number: ")
        
        if choice == '1':
            addPatient(patients)
        elif choice == '2':
            showPatients(patients)
        elif choice == '3':
            searchPatient(patients)
        elif choice == '4':
            removePatient(patients)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
