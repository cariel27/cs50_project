class BloodType:
    BLOOD_TYPES = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    O_POSITIVE_DONOR = ["O+", "O-"]
    O_POSITIVE_RECEIVER = ["O+", "A+", "B+", "AB+"]
    O_NEGATIVE_RECEIVER = BLOOD_TYPES
    O_NEGATIVE_DONOR = ["O-"]

    A_POSITIVE_RECEIVER = ["A+", "AB+"]
    A_POSITIVE_DONOR = ["A+", "A-", "O+", "O-"]
    A_NEGATIVE_RECEIVER = ["A+", "A-", "AB+", "AB-"]
    A_NEGATIVE_DONOR = ["A-", "O-"]

    B_POSITIVE_RECEIVER = ["B+", "AB+"]
    B_POSITIVE_DONOR = ["B+", "B-", "O-", "O+"]
    B_NEGATIVE_RECEIVER = ["B+", "B-", "AB+", "AB-"]
    B_NEGATIVE_DONOR = ["B-", "O-"]

    AB_POSITIVE_RECEIVER = ["AB+"]
    AB_POSITIVE_DONOR = BLOOD_TYPES
    AB_NEGATIVE_DONOR = ["A-", "B-", "AB-", "O-"]
    AB_NEGATIVE_RECEIVER = ["AB+", "AB-"]

    def __init__(self, antigen: str, protein: str):
        assert antigen, "Missing antigen."
        assert protein, "Missing protein."

        self.antigen = antigen
        self.protein = protein

    def __str__(self):
        return self.antigen + self.protein

    @classmethod
    def get_compatible_donors(cls, recipient_blood_type):
        blood_type = recipient_blood_type.__str__()
        assert blood_type in cls.BLOOD_TYPES, "Invalid blood type."

        if blood_type.__str__() == "O-":
            return cls.O_NEGATIVE_DONOR
        elif blood_type == "O+":
            return cls.O_POSITIVE_DONOR
        elif blood_type == "A-":
            return cls.A_NEGATIVE_DONOR
        elif blood_type == "A+":
            return cls.A_POSITIVE_DONOR
        elif blood_type == "B-":
            return cls.B_NEGATIVE_DONOR
        elif blood_type == "B+":
            return cls.B_POSITIVE_DONOR
        elif blood_type == "AB-":
            return cls.AB_NEGATIVE_DONOR
        elif blood_type == "AB+":
            return cls.AB_POSITIVE_DONOR

    @classmethod
    def get_compatible_receipts(cls, donor_blood_type):
        blood_type = donor_blood_type.__str__()
        assert blood_type in cls.BLOOD_TYPES, "Invalid blood type."

        if blood_type == "O-":
            return cls.O_NEGATIVE_RECEIVER
        elif blood_type == "O+":
            return cls.O_POSITIVE_RECEIVER
        elif blood_type == "A-":
            return cls.A_NEGATIVE_RECEIVER
        elif blood_type == "A+":
            return cls.A_POSITIVE_RECEIVER
        elif blood_type == "B-":
            return cls.B_NEGATIVE_RECEIVER
        elif blood_type == "B+":
            return cls.B_POSITIVE_RECEIVER
        elif blood_type == "AB-":
            return cls.AB_NEGATIVE_RECEIVER
        elif blood_type == "AB+":
            return cls.AB_POSITIVE_RECEIVER

    @classmethod
    def get_o_recipients(cls, protein: bool):
        types = list()
        types.append(BloodType(antigen="A", protein=False))
        types.append(BloodType(antigen="B", protein=False))
        types.append(BloodType(antigen="AB", protein=False))
        if not protein:
            types.append(BloodType(antigen="A", protein=True))
            types.append(BloodType(antigen="B", protein=True))
            types.append(BloodType(antigen="AB", protein=True))
        return types

    @classmethod
    def get_a_recipients(cls, protein: bool):
        types = list()
        types.append(BloodType(antigen="A", protein=True))
        types.append(BloodType(antigen="AB", protein=True))
        if not protein:
            types.append(BloodType(antigen="A", protein=False))
            types.append(BloodType(antigen="AB", protein=False))
        return types

    @classmethod
    def get_b_recipients(cls, protein: bool):
        types = list()
        types.append(BloodType(antigen="B", protein=True))
        types.append(BloodType(antigen="AB", protein=True))
        if not protein:
            types.append(BloodType(antigen="AB", protein=False))
            types.append(BloodType(antigen="B", protein=False))
        return types

    @classmethod
    def get_ab_recipients(cls, protein: bool):
        types = list()
        if protein:
            types.append(BloodType(antigen="AB", protein=True))
        else:
            types.append(BloodType(antigen="AB", protein=True))
            types.append(BloodType(antigen="AB", protein=False))
        return types

    @classmethod
    def calculate_recipient(cls, donor):
        if donor.antigen == "O":
            return cls.get_o_recipients(protein=donor.protein)
        elif donor.antigen == "A":
            return cls.get_a_recipients(protein=donor.protein)
        elif donor.antigen == "B":
            return cls.get_b_recipients(protein=donor.protein)
        elif donor.antigen == "AB":
            return cls.get_ab_recipients(protein=donor.protein)

    @property
    def antigen(self) -> str:
        return self._antigen

    @antigen.setter
    def antigen(self, antigen: str):
        self._antigen = antigen

    @property
    def protein(self) -> bool:
        return self._protein

    @protein.setter
    def protein(self, protein: bool):
        self._protein = protein
