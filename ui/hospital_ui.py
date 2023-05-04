import pyttsx3
import sys
from model.blood_type import BloodType
from db_helper.hospital_db import HospitalDb
from helper import helper

engine = None


def select_blood():
    blood_options = {"1": "A +", "2": "A -", "3": "B +", "4": "B -", "5": "AB +", "6": "AB -", "7": "O +", "8": "O -"}
    # Get user input for donor and recipient blood types
    print("#" * 65)
    for k, v in blood_options.items():
        print(f"{k}) {v}")
    print("or Press 'Q' to exit", end="\n")
    print("#" * 65)
    while True:
        option = input("Select blood type: ")
        if option in blood_options.keys():
            return blood_options[option]
        elif option.upper() == "Q":
            sys.exit("Bye.")


def select_patient(hospital_db: HospitalDb) -> str:
    # Get user input for donor and recipient blood types
    patient_ids = hospital_db.get_ids()
    helper.clear()
    print("=" * 65)
    print("WELCOME TO CS50 HOSPITAL")
    print("=" * 65)
    input("Press any key to continue...")
    while True:
        hospital_db.show_patients_by(criteria="all")
        print("#" * 65)
        print("<<<<<Select a Patient>>>>>")
        print("Type Patient ID")
        print("or Press 'Q' to exit", end="\n")
        print("#" * 65)
        option = input(">>> ")

        if option.upper() == "Q":
            helper.clear()
            hospital_db.delete_db()
            sys.exit("Bye.")
        elif option in patient_ids:
            helper.clear()
            patient = hospital_db.get_patient_by_id(int(option))
            say_patient_data(patient)
            show_patient_options(patient=patient, h_db=hospital_db)
        else:
            print("\n")
            print(f"Patient ID {option} does not exist.\n")


def show_patient_options(patient: HospitalDb, h_db):
    while True:
        print("=" * 65)
        print(">>>OPTIONS<<<")
        print("(1) Show Compatible Donors.")
        print("(2) Show Compatible Recipient.")
        print("(3) Show List of compatible patients.")
        print("(4) Back to previous Menu.", end="\n")
        print("#" * 65)
        option = input("Select an option: ")
        print()
        match option:
            case "1":
                helper.clear()
                compatible_donors = BloodType.get_compatible_donors(recipient_blood_type=patient["blood_type"])
                print("\nCompatible Donors: ", compatible_donors)
            case "2":
                helper.clear()
                compatible_recipient = BloodType.get_compatible_receipts(donor_blood_type=patient["blood_type"])
                print("\nCompatible Recipients: ", compatible_recipient)
            case "3":
                helper.clear()
                compatible_donors = BloodType.get_compatible_donors(recipient_blood_type=patient["blood_type"])
                h_db.show_patients_by("compatible blood", compatible_donors=compatible_donors, patient=patient)
            case "4":
                helper.clear()
                break
            case _:
                print("Invalid option")
                helper.clear()


def say_patient_data(patient):
    print("\n")
    print("#" * 65)
    print("Patient's First name", patient["first_name"])
    say("First name " + patient["first_name"])
    print("Last name", patient["last_name"])
    say("Last name " + patient["last_name"])
    print("Security Social Number", patient["ssn"])
    say("Security Social Number " + patient["ssn"].replace("-", ""))
    print("Blood type", patient["blood_type"])
    say("Blood type " + patient["blood_type"].replace("-", " Negative").replace("+", " Positive"))


def say(data: str):
    global engine
    if not engine:
        engine = pyttsx3.init(driverName=helper.get_driver())
    engine.say(data)
    engine.runAndWait()
