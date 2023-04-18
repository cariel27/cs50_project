class Person:
    def __init__(self, **kwargs):
        assert kwargs["first_name"], "Missing First Name"
        assert kwargs["last_name"], "Missing Last Name"
        assert kwargs["ssn"], "Missing SSN"

        self.first_name = kwargs["first_name"]
        self.last_name = kwargs["last_name"]
        self.ssn = kwargs["ssn"]

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def ssn(self):
        return self._ssn

    @ssn.setter
    def ssn(self, ssn: str):
        self._ssn = ssn