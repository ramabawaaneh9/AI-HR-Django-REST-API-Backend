
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import InterviewQuestionSet
from core.serializers import InterviewQuestionSetSerializer


class InterviewQuestionSetDetailAPIView(APIView):

    def get(self, request, pk):
        question_set = get_object_or_404(
            InterviewQuestionSet,
            pk=pk
        )

        serializer = InterviewQuestionSetSerializer(
            question_set
        )

        return Response(serializer.data)
