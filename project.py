from db_helper.hospital_db import HospitalDb
from ui import hospital_ui
import argparse

DB_NAME = "cs50_hospital"


def main():
    parser = argparse.ArgumentParser(description="CS50 Hospital.")
    parser.add_argument("-n", default=10, help="number patients", type=int)
    parser.add_argument("-v", default="OFF", choices=['ON', 'OFF'], help="If text-to-speech is ON/OFF. Default is Off",
                        type=str)
    args = parser.parse_args()

    # DB initialization
    h_db = HospitalDb(db_name=DB_NAME)
    h_db.db_setup()
    h_db.populate_db(rows_qty=args.n)

    # Select a patient
    hospital_ui.select_patient(hospital_db=h_db, is_voice_enabled=True if args.v == "ON" else False)

    # Clean Up
    h_db.delete_db()


if __name__ == "__main__":
    main()
