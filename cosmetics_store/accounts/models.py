from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from datetime import date

from cosmetics_store.accounts.validators import validator_check_only_letters_dashes_in_name, \
    validator_check_valid_phone_number


class StoreUserModel(auth_models.AbstractUser):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    MAX_FIRST_NAME_LENGTH = 20
    MAX_LAST_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 3
    MAX_PHONE_LENGTH = 10

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            validator_check_only_letters_dashes_in_name,
        ],
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(MIN_NAME_LENGTH),
            validator_check_only_letters_dashes_in_name,
        ],
    )

    phone = models.CharField(
        max_length=MAX_PHONE_LENGTH,
        null=True,
        blank=True,
        validators=[validator_check_valid_phone_number,]
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(limit_value=date(1900, 1, 1))
        ],
    )

    gender = models.CharField(
        max_length=8,
        choices=GENDER_CHOICES,
    )

    def __str__(self):
        return f"User: {self.username}"


    # @property
    # def current_age(self):
    #     today = date.today()
    #     age = relativedelta(today, self.date_of_birth).years
    #     return age





