import re
from django.core.exceptions import ValidationError


def validator_check_only_letters_dashes_in_name(value):
    match = re.match(r"^[A-Za-z]+-?[A-Za-z]+$", value)
    if not match:
        raise ValidationError("The name can contains only letters and one dash e.t. Anna-Maria.")


def validator_check_valid_phone_number(value):
    match = re.match(r"^0\d{9}$", value)
    if not match:
        raise ValidationError("Please, enter valid phone number e.t. 0#########!")
