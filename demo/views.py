from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import MedicationReminder
from .forms import MedicationReminderForm


def reminders(request):
    """
    Näyttää lomakkeen + listan.
    POST: lisää uuden muistutuksen (PRG-malli).
    """
    if request.method == "POST":
        form = MedicationReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reminders")
    else:
        form = MedicationReminderForm()

    items = MedicationReminder.objects.all()
    return render(request, "demo/reminders.html", {"form": form, "items": items})


@require_POST
def reminder_delete(request, pk):
    item = get_object_or_404(MedicationReminder, pk=pk)
    item.delete()
    return redirect("reminders")