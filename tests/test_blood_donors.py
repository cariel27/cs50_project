from model.blood_type import BloodType


def test_donors_for_blood_type_a_positive():
    a_positive = BloodType(antigen="A", protein="+")
    assert BloodType.get_compatible_donors(recipient_blood_type=a_positive) == BloodType.A_POSITIVE_DONOR


def test_donors_for_blood_type_a_negative():
    a_negative = BloodType(antigen="A", protein="-")
    assert BloodType.get_compatible_donors(recipient_blood_type=a_negative) == BloodType.A_NEGATIVE_DONOR


def test_donors_for_blood_type_b_positive():
    b_positive = BloodType(antigen="B", protein="+")
    assert BloodType.get_compatible_donors(recipient_blood_type=b_positive) == BloodType.B_POSITIVE_DONOR


def test_donors_for_blood_type_b_negative():
    b_positive = BloodType(antigen="B", protein="-")
    assert BloodType.get_compatible_donors(recipient_blood_type=b_positive) == BloodType.B_NEGATIVE_DONOR


def test_donors_for_blood_type_ab_positive():
    ab_positive = BloodType(antigen="AB", protein="+")
    assert BloodType.get_compatible_donors(recipient_blood_type=ab_positive) == BloodType.AB_POSITIVE_DONOR


def test_donors_for_blood_type_ab_negative():
    ab_negative = BloodType(antigen="AB", protein="-")
    assert BloodType.get_compatible_donors(recipient_blood_type=ab_negative) == BloodType.AB_NEGATIVE_DONOR


def test_donors_for_blood_type_o_positive():
    o_positive = BloodType(antigen="O", protein="+")
    assert BloodType.get_compatible_donors(recipient_blood_type=o_positive) == BloodType.O_POSITIVE_DONOR


def test_donors_for_blood_type_o_positive():
    o_negative = BloodType(antigen="O", protein="-")
    assert BloodType.get_compatible_donors(recipient_blood_type=o_negative) == BloodType.O_NEGATIVE_DONOR
