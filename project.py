from db_helper.hospital_db import HospitalDb
import sys

BLOOD_OPTIONS = {"1": "A +", "2": "A -", "3": "B +", "4": "B -", "5": "AB +", "6": "AB -", "7": "O +", "8": "O -"}


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


def main():
    h_db = HospitalDb(db_name="cs50_hospital")
    h_db.db_setup()
    h_db.populate_db()


    # antigen, protein = select_blood().split(" ")
    # patient_blood_type = BloodType(antigen=antigen, protein=protein)
    #
    # a = BloodType.get_compatible_donors(recipient_blood_type=patient_blood_type)
    # print("Compatible Donors: ", a)
    # b = BloodType.get_compatible_receipts(donor_blood_type=patient_blood_type)
    # print("Compatible Receiver: ", b)


if __name__ == "__main__":
    main()
