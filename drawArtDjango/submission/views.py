# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (
    CreateAPIView, UpdateAPIView
)

from submission.models import Submission
from submission.serializers import SubmissionSerializer


class SubmissionCreate(CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class SubmissionUpdate(UpdateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    lookup_url_kwarg = 'submission_id'
