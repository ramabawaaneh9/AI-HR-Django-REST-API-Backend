
from django.urls import path
from core.views.interview import interview_question_set_detail

urlpatterns = [
    path(
        'interview-questions/<int:pk>/',
        interview_question_set_detail,
        name='interview-question-detail'
    ),
]
