
from rest_framework import serializers
from core.models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer):

    department_name = serializers.CharField(
        source="department.name",
        read_only=True
    )

    class Meta:
        model = JobPosition

        fields = [
            "id",
            "department",
            "department_name",
            "title",
            "description",
            "required_skills",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate_required_skills(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Required skills must be a list."
            )

        if not all(
            isinstance(skill, str) and skill.strip()
            for skill in value
        ):
            raise serializers.ValidationError(
                "Each skill must be a non-empty string."
            )

        return value
