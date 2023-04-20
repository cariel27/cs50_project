from db_helper.hospital_db import HospitalDb
import sys
import os
import cowsay
import pyttsx3

BLOOD_OPTIONS = {"1": "A +", "2": "A -", "3": "B +", "4": "B -", "5": "AB +", "6": "AB -", "7": "O +", "8": "O -"}
DB_NAME = "cs50_hospital"


def select_blood():
    # Get user input for donor and recipient blood types
    print("#" * 65)
    for k, v in BLOOD_OPTIONS.items():
        print(f"{k}) {v}")
    print("or Press 'Q' to exit", end="\n")
    print("#" * 65)
    while True:
        option = input("Select blood type: ")
        if option in BLOOD_OPTIONS.keys():
            return BLOOD_OPTIONS[option]
        elif option.upper() == "Q":
            sys.exit("Bye.")


def select_patient(patient_ids: []) -> str:
    # Get user input for donor and recipient blood types
    print("#" * 65)
    print("Select a patient")
    print("or Press 'Q' to exit", end="\n")
    print("#" * 65)
    while True:
        option = input("ID: ")
        if option.upper() == "Q":
            sys.exit("Bye.")
        elif option in patient_ids:
            return option
        else:
            print(f"{option} does not exist.")


def delete_db():
    db_path = os.path.dirname(os.path.abspath(__file__)) + "/" + DB_NAME + ".pdl"
    if os.path.exists(db_path):
        os.remove(db_path)
        print("DB File deleted successfully.")
    else:
        print("DB file does not exist.")


def say_patient_data(patient):
    engine = pyttsx3.init()
    for d in patient:
        cowsay.cow(d)
        engine.say(d)
        engine.runAndWait()


def main():
    # DB initialization
    h_db = HospitalDb(db_name=DB_NAME)
    h_db.db_setup()
    h_db.populate_db()
    h_db.show_patients()

    # Select a patient
    patient = select_patient(patient_ids=h_db.get_ids())
    say_patient_data(h_db.get_patient_by_id(int(patient)))

    # antigen, protein = select_blood().split(" ")
    # patient_blood_type = BloodType(antigen=antigen, protein=protein)
    #
    # a = BloodType.get_compatible_donors(recipient_blood_type=patient_blood_type)
    # print("Compatible Donors: ", a)
    # b = BloodType.get_compatible_receipts(donor_blood_type=patient_blood_type)
    # print("Compatible Receiver: ", b)

    # Clean Up
    delete_db()


if __name__ == "__main__":
    main()
