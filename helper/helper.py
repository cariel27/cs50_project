import pyttsx3
import sys
from os.path import dirname, abspath
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_project_path():
    return dirname(dirname(abspath(__file__)))


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


def say_patient_data(patient):
    print("\n")
    print("#" * 65)
    print("Patient's First name", patient["first_name"])
    print("Patient's Last name", patient["last_name"])
    print("SSN", patient["ssn"])
    print("Blood type", patient["blood_type"])
    say(patient["first_name"])
    say(patient["last_name"])
    say(patient["ssn"])
    say(patient["blood_type"])


def say(data: str):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
