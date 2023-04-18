from .person import Person


class Doctor(Person):
    def __init__(self, registration_number: str, **kwargs):
        super().__init__(kwargs)
        assert registration_number, "Missing Registration number"
        self.registration_number = registration_number

