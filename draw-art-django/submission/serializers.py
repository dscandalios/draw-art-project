from rest_framework import serializers

from submission.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = ('id', 'name', 'info', 'feelings', 'email')
