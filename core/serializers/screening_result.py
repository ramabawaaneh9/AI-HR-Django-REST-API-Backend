
from rest_framework import serializers
from core.models import ScreeningResult


class ScreeningResultSerializer(serializers.ModelSerializer):

    candidate_name = serializers.CharField(
        source="candidate.full_name",
        read_only=True
    )

    job_position_title = serializers.CharField(
        source="job_position.title",
        read_only=True
    )

    class Meta:
        model = ScreeningResult

        fields = [
            "id",
            "candidate",
            "candidate_name",
            "job_position",
            "job_position_title",
            "score",
            "strengths",
            "missing_skills",
            "recommendation",
            "summary",
            "raw_report",
            "generated_at",
        ]

        read_only_fields = fields
