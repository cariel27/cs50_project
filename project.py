from db_helper.hospital_db import HospitalDb
from model.blood_type import BloodType
from helper import helper
import sys


DB_NAME = "cs50_hospital"


def select_patient(patient_ids: []) -> str:
    # Get user input for donor and recipient blood types
    while True:
        print("#" * 65)
        print(">>>Select a Patient<<<")
        print("Type Patient ID: ")
        print("or Press 'Q' to exit", end="\n")
        print("#" * 65)
        option = input("ID: ")

        if option.upper() == "Q":
            helper.clear()
            sys.exit("Bye.")
        elif option in patient_ids:
            # FIXME: CHECK HOW TO GET PATIENT INFO BY ID
            # h_db.get_patient_by_id(int(option))
            return option
        else:
            print("\n")
            print(f"Patient with ID {option} does not exist.\n")


def main():
    # DB initialization
    h_db = HospitalDb(db_name=DB_NAME)
    h_db.db_setup()
    h_db.populate_db()
    h_db.show_patients()

    # Select a patient
    patient = select_patient(patient_ids=h_db.get_ids())
    patient = h_db.get_patient_by_id(int(patient))
    # helper.say_patient_data(patient)
    a = BloodType.get_compatible_donors(recipient_blood_type=patient["blood_type"])
    print("\nCompatible Donors: ", a)
    # helper.say(data=f"The compatible donors for {patient['blood_type']} are" + a)

    # b = BloodType.get_compatible_receipts(donor_blood_type=patient_blood_type)
    # print("Compatible Receiver: ", b)

    # Clean Up
    h_db.delete_db()


if __name__ == "__main__":
    main()
