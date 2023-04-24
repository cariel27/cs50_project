from db_helper.hospital_db import HospitalDb
from model.blood_type import BloodType
from helper import helper
import sys

DB_NAME = "cs50_hospital"


def select_patient(hospital_db: HospitalDb) -> str:
    # Get user input for donor and recipient blood types
    patient_ids = hospital_db.get_ids()
    print("=" * 65)
    print("WELCOME TO CS50 HOSPITAL")
    print("=" * 65)
    input("Press any key to continue...")
    while True:
        hospital_db.show_patients_by(criteria="all")
        print("#" * 65)
        print("<<<<<Select a Patient>>>>>")
        print("Type Patient ID: ")
        print("or Press 'Q' to exit", end="\n")
        print("#" * 65)
        option = input("ID: ")

        if option.upper() == "Q":
            helper.clear()
            hospital_db.delete_db()
            sys.exit("Bye.")
        elif option in patient_ids:
            helper.clear()
            patient = hospital_db.get_patient_by_id(int(option))
            helper.say_patient_data(patient)
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
        print("(3) Show List of Patients compatible.")
        print("(4) Back to previous Menu.", end="\n")
        print("#" * 65)
        option = input("Select an option: ")
        print()
        match option:
            case "1":
                compatible_donors = BloodType.get_compatible_donors(recipient_blood_type=patient["blood_type"])
                print("\nCompatible Donors: ", compatible_donors)
            case "2":
                compatible_recipient = BloodType.get_compatible_receipts(donor_blood_type=patient["blood_type"])
                print("\nCompatible Recipients: ", compatible_recipient)
            case "3":
                compatible_donors = BloodType.get_compatible_donors(recipient_blood_type=patient["blood_type"])
                h_db.show_patients_by("compatible blood", compatible_donors=compatible_donors, patient=patient)
            case "4":
                helper.clear()
                break
            case _:
                print("Invalid option")
                helper.clear()


def main():
    # DB initialization
    h_db = HospitalDb(db_name=DB_NAME)
    h_db.db_setup()
    h_db.populate_db(rows_qty=20)

    # Select a patient
    select_patient(hospital_db=h_db)

    # Clean Up
    h_db.delete_db()


if __name__ == "__main__":
    main()
