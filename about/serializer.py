from rest_framework import serializers
# model
from .models import details

class serializerDetails(serializers.ModelSerializer):
    class Meta:
        model=details
        fields=("id","surname","contact","salary","address","date_Time")