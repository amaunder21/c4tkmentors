from django.db import models
from django.contrib.auth.models import User
from mentorlol import settings

# Create your models here.
class UserProfile(models.Model):
    MARITAL_STATUS_MARRIED = "married"
    MARITAL_STATUS_SINGLE = "single"
    MARITAL_STATUS_RELATIONSHOP = "in_a_relationship"
    MARITAL_STATUS_DIVORCED = "divorced"

    MARITAL_STATUSES = (
        (MARITAL_STATUS_MARRIED, "Married"),
        (MARITAL_STATUS_SINGLE, "Single"),
        (MARITAL_STATUS_RELATIONSHOP, "In a Relationship"),
        (MARITAL_STATUS_DIVORCED, "Divorced")
    )

    STATES = [
        "new",
        "matched"
    ]

    user = models.OneToOneField(User, verbose_name="The user this profile belongs to")
    name = models.CharField(max_length=settings.DEFAULT_CHAR_LENGTH)
    emailAddress = models.EmailField()
    dateOfBirth = models.DateField()
    location = models.CharField(max_length=settings.DEFAULT_CHAR_LENGTH)
    occupation = models.CharField(max_length=settings.DEFAULT_CHAR_LENGTH)
    maritalStatus = models.CharField(
        max_length=settings.DEFAULT_CHAR_LENGTH,
        choices=MARITAL_STATUSES
        )
    kids = models.CharField(max_length=settings.DEFAULT_CHAR_LENGTH)
    education = models.CharField(max_length=settings.DEFAULT_CHAR_LENGTH)
    interests = models.TextField()
    lifeExperience = models.TextField()
    skills = models.TextField()
