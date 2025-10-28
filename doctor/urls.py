from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ConsultationViewSet, PrescriptionHistoryViewSet

router = DefaultRouter()
router.register(r"consultations", ConsultationViewSet, basename="consultations")
router.register(r"prescriptions", PrescriptionHistoryViewSet, basename="prescriptions")  # ✅ fixed quote

urlpatterns = [
    path("api/", include(router.urls)),
]
