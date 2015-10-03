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

    state = models.CharField("State",
        max_length=settings.DEFAULT_CHAR_LENGTH,
        default=STATES[0])
    user = models.OneToOneField(User, verbose_name="User")
    name = models.CharField("Full Name", max_length=settings.DEFAULT_CHAR_LENGTH)
    date_of_birth = models.DateField("Date of Birth")
    location = models.CharField("Location", max_length=settings.DEFAULT_CHAR_LENGTH)
    occupation = models.CharField("Occupation", max_length=settings.DEFAULT_CHAR_LENGTH)
    marital_status = models.CharField("Marital Status",
        max_length=settings.DEFAULT_CHAR_LENGTH,
        choices=MARITAL_STATUSES
        )
    kids = models.CharField("Children", max_length=settings.DEFAULT_CHAR_LENGTH)
    education = models.CharField("Education", max_length=settings.DEFAULT_CHAR_LENGTH)
    interests = models.TextField("Interests")
    life_experience = models.TextField("Life Experience")
    skills = models.TextField("Skills")

    def __unicode__(self):
        return self.name
