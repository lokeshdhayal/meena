from .models import Queries
from rest_framework import serializers

class serilizer(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields ="__all__"
