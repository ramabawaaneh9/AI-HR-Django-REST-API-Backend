
from rest_framework import serializers
from core.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate

        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate_full_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Full name cannot be empty."
            )
        return value.strip()
