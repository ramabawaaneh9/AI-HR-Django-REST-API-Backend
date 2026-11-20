
import re

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

    def validate_phone(self, value):
        value = value.strip()

        if not re.fullmatch(r"\+?[0-9]{7,15}", value):
            raise serializers.ValidationError(
                "Phone number must contain 7 to 15 digits, "
                "with an optional + at the beginning."
            )

        return value
