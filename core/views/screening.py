
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import ScreeningResult
from core.serializers import ScreeningResultSerializer


@api_view(['GET'])
def screening_result_detail(request, pk):
    screening = get_object_or_404(
        ScreeningResult,
        pk=pk
    )

    serializer = ScreeningResultSerializer(screening)

    return Response(serializer.data)
