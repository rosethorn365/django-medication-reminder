from django.urls import path
from .views import reminders, reminder_delete

urlpatterns = [
    path("reminders/", reminders, name="reminders"),
    path("reminders/<int:pk>/delete/", reminder_delete, name="reminder_delete"),
]