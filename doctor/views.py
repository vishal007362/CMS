from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Consultation, Prescription
from .serializers import ConsultationSerializer, PrescriptionSerializer


class ConsultationViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only endpoints for consultation history."""

    queryset = (
        Consultation.objects.select_related("patient", "doctor")
        .prefetch_related("prescriptions")
        .order_by("-date")
    )
    serializer_class = ConsultationSerializer

    @action(detail=False, methods=["get"], url_path=r"patient/(?P<patient_id>\d+)")
    def by_patient(self, request, patient_id=None):
        """/consultations/patient/<id>/ - consultations for a patient."""

        consultations = self.queryset.filter(patient_id=patient_id)
        page = self.paginate_queryset(consultations)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(consultations, many=True)
        return Response(serializer.data)


class PrescriptionHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only endpoints for prescription history."""

    queryset = (
        Prescription.objects.select_related("consultation", "consultation__patient")
        .order_by("-consultation__date")
    )
    serializer_class = PrescriptionSerializer

    @action(
        detail=False,
        methods=["get"],
        url_path=r"medicine/history/patient/(?P<patient_id>\d+)",
    )
    def medicine_history_by_patient(self, request, patient_id=None):
        """/prescriptions/medicine/history/patient/<id>/ - prescriptions for a patient."""

        prescriptions = self.queryset.filter(consultation__patient_id=patient_id)
        page = self.paginate_queryset(prescriptions)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(prescriptions, many=True)
        return Response(serializer.data)