from .models import temp_log
from rest_framework import serializers

class tempSerializer(serializers.ModelSerializer):
    class Meta:
        model = temp_log
        fields = '__all__'