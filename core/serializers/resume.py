
from pathlib import Path

from rest_framework import serializers
from core.models import Resume


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume

        fields = [
            "id",
            "candidate",
            "file",
            "uploaded_at",
        ]

        read_only_fields = [
            "id",
            "uploaded_at",
        ]

    def validate_file(self, value):
        allowed_extensions = {".pdf", ".docx", ".txt"}

        extension = Path(value.name).suffix.lower()

        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Only PDF, DOCX and TXT files are allowed."
            )

        max_size = 5 * 1024 * 1024

        if value.size > max_size:
            raise serializers.ValidationError(
                "File size must not exceed 5 MB."
            )

        return value
