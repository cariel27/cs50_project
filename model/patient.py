from .blood_type import BloodType
from .doctor import Doctor
from .person import Person


class Patient(Person):
    def __init__(self, **kwargs):
        self.doctor = []
        if kwargs.get("weight", False):
            self.weight = kwargs["weight"]
        if kwargs.get("height", False):
            self.height = kwargs["height"]
        if kwargs.get("doctor", False):
            self.doctor = kwargs["doctor"]
        if kwargs.get("blood_type", False):
            self.blood_type = kwargs["blood_type"]

    def __init__(self, first_name: str, last_name: str, ssn: str, **kwargs):
        super().__init__(first_name=first_name, last_name=last_name, ssn=ssn)
        if kwargs:
            self.__init__(kwargs=kwargs)

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        self._weight = weight

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float):
        self._height = height

    @property
    def doctor(self) -> Doctor:
        return self._doctor

    @doctor.setter
    def doctor(self, doctor: Doctor):
        self._doctor.append(doctor)

    @property
    def blood_type(self) -> BloodType:
        return self._blood_type

    @blood_type.setter
    def blood_type(self, blood_type: BloodType):
        self._blood_type = blood_type
