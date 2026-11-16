
from rest_framework import serializers
from core.models import InterviewQuestionSet


class InterviewQuestionSetSerializer(serializers.ModelSerializer):

    candidate_name = serializers.CharField(
        source="candidate.full_name",
        read_only=True
    )

    job_position_title = serializers.CharField(
        source="job_position.title",
        read_only=True
    )

    class Meta:
        model = InterviewQuestionSet

        fields = [
            "id",
            "candidate",
            "candidate_name",
            "job_position",
            "job_position_title",
            "screening_result",
            "technical_questions",
            "behavioral_questions",
            "follow_up_questions",
            "generated_at",
        ]

        read_only_fields = fields
