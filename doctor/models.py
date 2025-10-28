from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_profile")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

    class Meta:
        ordering = ["user__first_name", "user__last_name"]  # ✅ Corrected field references

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="consultations")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_consultations")
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def _str_(self):
        return f"Consult #{self.pk} - {self.patient} (Dr. {self.doctor})"


class Prescription(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="prescriptions")
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.medicine_name} » {self.consultation.patient}"