import pyttsx3
import sys
from os.path import dirname, abspath
import os
import platform

engine = None


def get_driver() -> str:
    op_sys = platform.platform()

    if "macOS" in op_sys:
        return "nsss"
    elif "Windows" in op_sys:
        return "sapi5"
    else:
        raise Exception("Not supported platform.")


def clear():
    for i in range(10):
        print()


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
        engine = pyttsx3.init(driverName=get_driver())
    engine.say(data)
    engine.runAndWait()
