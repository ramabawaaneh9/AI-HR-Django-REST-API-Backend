
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import ScreeningResult
from core.serializers import ScreeningResultSerializer


class ScreeningResultDetailAPIView(APIView):

    def get(self, request, pk):
        screening = get_object_or_404(
            ScreeningResult,
            pk=pk
        )

        serializer = ScreeningResultSerializer(screening)

        return Response(serializer.data)
