from random import choice
import random
from faker import Faker
from pydblite import Base
from model.patient import Patient
from model.person import Person
from model.blood_type import BloodType


class HospitalDb:
    def __init__(self, db_name="patients"):
        self.db = Base(f'./{db_name}.pdl')

    def db_setup(self):
        properties_list = [prop for prop in dir(Patient) if
                           isinstance(getattr(Patient, prop), property) and (
                                   prop in vars(Patient) or prop in vars(Person))]
        self.db.create(*properties_list, mode="open")

    def populate_db(self, rows_qty=3):
        f = Faker()
        for _ in range(rows_qty):
            self.db.insert(
                blood_type=choice(BloodType.BLOOD_TYPES), doctor=f.name(), first_name=f.name(),
                height=random.uniform(3.0, 6.0),
                last_name=f.name(),
                ssn=f.ssn(), weight=random.uniform(22, 330))
            self.db.insert(first_name=f.name(), last_name=f.name(), ssn=f.ssn(),
                           blood_type=choice(BloodType.BLOOD_TYPES),
                           height=random.uniform(3.0, 6.0),
                           weight=random.uniform(22, 330),
                           doctor=f.name())
        self.db.commit()
        for r in self.db:
            print(r)
