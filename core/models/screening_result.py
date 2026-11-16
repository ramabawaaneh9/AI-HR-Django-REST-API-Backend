
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .candidate import Candidate
from .job_position import JobPosition


class ScreeningResult(models.Model):

    class Recommendation(models.TextChoices):
        PROCEED = "proceed", "Proceed"
        HOLD = "hold", "Hold"
        REJECT = "reject", "Reject"

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.PROTECT,
        related_name="screening_results"
    )

    job_position = models.ForeignKey(
        JobPosition,
        on_delete=models.PROTECT,
        related_name="screening_results"
    )

    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    strengths = models.JSONField(default=list)

    missing_skills = models.JSONField(default=list)

    recommendation = models.CharField(
        max_length=10,
        choices=Recommendation.choices
    )

    summary = models.TextField()

    raw_report = models.JSONField(default=dict)

    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "screening_results"
        ordering = ["-generated_at"]

    def __str__(self):
        return f"{self.candidate.full_name} - {self.score}/100"
