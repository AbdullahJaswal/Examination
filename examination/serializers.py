from .models import *

from rest_framework import serializers


class UserProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProduct
		fields = "__all__"


class SubmissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Submission
		fields = "__all__"
