from django.db import models

class MedicationReminder(models.Model):
    medication_name = models.CharField(max_length=120)
    dosage = models.CharField(max_length=120, blank=True)
    time_of_day = models.TimeField()
    instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["time_of_day", "-created_at"]

    def __str__(self):
        dosage_part = f" ({self.dosage})" if self.dosage else ""
        return f"{self.medication_name}{dosage_part} @ {self.time_of_day}"

        