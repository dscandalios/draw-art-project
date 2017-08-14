from django.conf.urls import url

from submission.views import (
    SubmissionCreate, SubmissionUpdate
)

urlpatterns = [
    url(r'(?P<submission_id>\d+)/?$', SubmissionUpdate.as_view()),
    url(r'', SubmissionCreate.as_view()),
]
