from django.contrib import admin
from .models import Patient, Consultation, Prescription


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_birth", "gender")
    search_fields = ("user_first_name", "userlast_name", "user_username")


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "date")
    list_filter = ("doctor",)
    search_fields = ("patient_userfirst_name", "patientuser_last_name")
    date_hierarchy = "date"


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("medicine_name", "consultation", "dosage", "duration")
    search_fields = ("medicine_name", "consultation_patientuser_first_name")