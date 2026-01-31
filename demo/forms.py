from django import forms
from .models import MedicationReminder


class MedicationReminderForm(forms.ModelForm):
    class Meta:
        model = MedicationReminder
        fields = ["medication_name", "dosage", "time_of_day", "instructions"]
        widgets = {
            "medication_name": forms.TextInput(attrs={
                "placeholder": "Esim. Burana",
                "style": "font-size: 18px; padding: 10px; width: 100%;"
            }),
            "dosage": forms.TextInput(attrs={
                "placeholder": "Esim. 1 tabletti / 10 mg",
                "style": "font-size: 18px; padding: 10px; width: 100%;"
            }),
            "time_of_day": forms.TimeInput(attrs={
                "type": "time",
                "style": "font-size: 18px; padding: 10px; width: 100%;"
            }),
            "instructions": forms.Textarea(attrs={
                "placeholder": "Esim. ruoan kanssa / tyhjään mahaan",
                "rows": 3,
                "style": "font-size: 18px; padding: 10px; width: 100%;"
            }),
        }

    def clean_medication_name(self):
        name = self.cleaned_data["medication_name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Lääkkeen nimen tulee olla vähintään 2 merkkiä.")
        return name