from django.contrib import admin
from .models import MedicationReminder

@admin.register(MedicationReminder)
class MedicationReminderAdmin(admin.ModelAdmin):
    list_display = ("medication_name", "dosage", "time_of_day", "created_at")
    list_filter = ("time_of_day",)
    search_fields = ("medication_name", "dosage", "instructions")
    