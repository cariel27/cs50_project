from random import choice
import random
from faker import Faker
from pydblite import Base
import helper.helper
from model.patient import Patient
from model.person import Person
from model.blood_type import BloodType
from tabulate import tabulate
import os


class HospitalDb:
    def __init__(self, db_name: str):
        self.db_path = helper.helper.get_project_path() + "/" + db_name + ".pdl"
        self.db = Base(self.db_path)

    def db_setup(self):
        """
        Creates in-memory DB for patient data by using the Patient class data model.
        :return:
        """
        properties_list = [prop for prop in dir(Patient) if
                           isinstance(getattr(Patient, prop), property) and (
                                   prop in vars(Patient) or prop in vars(Person))]
        self.db.create(*properties_list, mode="open")

    def populate_db(self, rows_qty=10):
        """
        Populates in-memory DB with random patient data generate with faker library.
        :param rows_qty: nbr of patients. Default = 10
        :return:
        """
        f = Faker()
        for _ in range(rows_qty):
            self.db.insert(first_name=f.name(), last_name=f.name(), ssn=f.ssn(),
                           blood_type=choice(BloodType.BLOOD_TYPES),
                           height=round(random.uniform(3.0, 6.0), 2),
                           weight=round(random.uniform(22, 330), 2),
                           doctor=f.name())
        self.db.commit()

    def show_patients_by(self, criteria, **kwargs):
        headers = ["ID", "First Name", "Last Name", "SSN", "Blood Type"]

        match criteria.upper():
            case "ALL":
                data = [[r['__id__'], r['first_name'], r['last_name'], r['ssn'], r['blood_type']] for r in self.db]
            case "COMPATIBLE BLOOD":
                print("COMPATIBLE PATIENTS")
                data = [[r['__id__'], r['first_name'], r['last_name'], r['ssn'], r['blood_type']] for r in self.db if
                        r["blood_type"] in kwargs["compatible_donors"] and r['ssn'] != kwargs["patient"]["ssn"]]
            case _:
                raise ValueError("Invalid Criteria.")
        table = tabulate(data, headers=headers, tablefmt="simple_grid")
        print(table)

    def get_ids(self):
        ids = [str(r["__id__"]) for r in self.db]
        return ids

    def get_patient_by_id(self, patient_id: int):
        return self.db(__id__=patient_id)[0]

    def delete_db(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            print("DB File deleted successfully.")
        else:
            print("DB file does not exist.")
