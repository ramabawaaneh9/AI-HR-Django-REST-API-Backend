from django.urls import path

from core.views import (
    DepartmentCreateAPIView,
    JobPositionCreateAPIView, CandidateCreateAPIView,
    ResumeUploadAPIView, ScreeningResultDetailAPIView, InterviewQuestionSetDetailAPIView
)

urlpatterns = [
    path(
        "departments/",
        DepartmentCreateAPIView.as_view(),
        name="department-create"
    ),
    path(
        "jobs/",
        JobPositionCreateAPIView.as_view(),
        name="job-position-create"
    ),

    path(
        "candidates/",
        CandidateCreateAPIView.as_view(),
        name="candidate-create"
    ),

path(
    "resumes/",
    ResumeUploadAPIView.as_view(),
    name="resume-upload"
),

path(
    "screenings/<int:pk>/",
    ScreeningResultDetailAPIView.as_view(),
    name="screening-result-detail"
),

path(
    "interviews/<int:pk>/",
    InterviewQuestionSetDetailAPIView.as_view(),
    name="interview-question-set-detail"
),
]