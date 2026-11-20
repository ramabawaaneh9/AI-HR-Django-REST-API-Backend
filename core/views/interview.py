
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import InterviewQuestionSet
from core.serializers import InterviewQuestionSetSerializer


@api_view(['GET'])
def interview_question_set_detail(request, pk):
    question_set = get_object_or_404(
        InterviewQuestionSet,
        pk=pk
    )

    serializer = InterviewQuestionSetSerializer(
        question_set
    )

    return Response(serializer.data)
