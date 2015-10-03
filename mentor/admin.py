from django.contrib import admin
from .models import UserProfile, Mentorship

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ("desires_mentor", "desires_mentoree", "state", "marital_status")

@admin.register(Mentorship)
class MentorshipAdmin(admin.ModelAdmin):
    list_display = ("id", "mentor", "mentoree")
