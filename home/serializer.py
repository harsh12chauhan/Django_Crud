from rest_framework import serializers
from .models import userDetails

class serializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ("id","name","email","password")