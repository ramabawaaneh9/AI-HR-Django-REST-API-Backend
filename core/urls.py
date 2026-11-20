
from django.urls import path

from core.views.department import department_create
from core.views.job_position import job_position_create
from core.views.candidate import candidate_create
from core.views.resume import resume_upload
from core.views.screening import screening_result_detail
from core.views.interview import interview_question_set_detail


urlpatterns = [
    path(
        "departments/",
        department_create,
        name="department-create"
    ),

    path(
        "jobs/",
        job_position_create,
        name="job-position-create"
    ),

    path(
        "candidates/",
        candidate_create,
        name="candidate-create"
    ),

    path(
        "resumes/",
        resume_upload,
        name="resume-upload"
    ),

    path(
        "screenings/<int:pk>/",
        screening_result_detail,
        name="screening-result-detail"
    ),

    path(
        "interviews/<int:pk>/",
        interview_question_set_detail,
        name="interview-question-set-detail"
    ),
]
