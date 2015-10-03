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

    STATE_NEW = "new"
    STATE_AWAITING_MATCH = "awaiting_match"
    STATE_MATCHED = "matched"

    STATES = (
        (STATE_NEW, "New"),
        (STATE_AWAITING_MATCH, "Awaiting Match"),
        (STATE_MATCHED, "Matched")
    )

    state = models.CharField("State",
        max_length=settings.DEFAULT_CHAR_LENGTH,
        default=STATE_NEW,
        choices=STATES)
    user = models.OneToOneField(User, verbose_name="User")
    desires_mentor = models.BooleanField("Wants a Mentor", default=False)
    mentor_bio = models.TextField("Mentor Biography", null=True)
    desires_mentoree = models.BooleanField("Wants a Mentoree", default=False)
    mentoree_bio = models.TextField("Mentoree Biography", null=True)
    name = models.CharField("Full Name", max_length=settings.DEFAULT_CHAR_LENGTH, null=True)
    date_of_birth = models.DateField("Date of Birth", null=True)
    location = models.CharField("Location", max_length=settings.DEFAULT_CHAR_LENGTH, null=True)
    occupation = models.CharField("Occupation", max_length=settings.DEFAULT_CHAR_LENGTH, null=True)
    marital_status = models.CharField("Marital Status",
        max_length=settings.DEFAULT_CHAR_LENGTH,
        choices=MARITAL_STATUSES,
        null=True
        )
    kids = models.CharField("Children", max_length=settings.DEFAULT_CHAR_LENGTH, null=True)
    education = models.CharField("Education", max_length=settings.DEFAULT_CHAR_LENGTH, null=True)
    interests = models.TextField("Interests", null=True)
    life_experience = models.TextField("Life Experience", null=True)
    skills = models.TextField("Skills", null=True)

    def __unicode__(self):
        if self.name != None:
            return self.name
        else:
            return self.user.email

class Mentorship(models.Model):
    mentor = models.OneToOneField(UserProfile,
        verbose_name="Mentor",
        related_name="mentor",
        limit_choices_to={ "desires_mentor": True })
    mentoree = models.OneToOneField(UserProfile,
        verbose_name="Mentoree",
        related_name="mentoree",
        limit_choices_to={ "desires_mentoree": True })
